# Copyright (C) GRyCAP - I3M - UPV
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
from enum import Enum
from tabulate import tabulate
import scar.logger as logger
from scar.utils import StrUtils


class OutputType(Enum):
    PLAIN_TEXT = 1
    JSON = 2
    VERBOSE = 3
    BINARY = 4


def parse_http_response(response, function_name, asynch, output_type, output_file):
    if response.ok:
        if output_type == OutputType.BINARY:
            with open(output_file, "wb") as out:
                out.write(StrUtils.decode_base64(response.text))
            text_message = f"Output saved in file '{output_file}'"
        else:
            text_message = f"Request Id: {response.headers['amz-lambda-request-id']}"
            if asynch:
                text_message += f"\nFunction '{function_name}' launched correctly"
            else:
                text_message += f"\nLog Group Name: {response.headers['amz-log-group-name']}\n"
                text_message += f"Log Stream Name: {response.headers['amz-log-stream-name']}\n"
                text_message += json.loads(response.text)["udocker_output"]
    else:
        if asynch and response.status_code == 502:
            text_message = f"Function '{function_name}' launched sucessfully."
        else:
            error = json.loads(response.text)
            if 'message' in error:
                text_message = f"Error ({response.reason}): {error['message']}"
            else:
                text_message = f"Error ({response.reason}): {error['exception']}"
    logger.info(text_message)


def _print_generic_response(response, output_type, aws_output, text_message=None, json_output=None, verbose_output=None, output_file=None):
    if output_type == OutputType.BINARY:
        with open(output_file, "wb") as out:
            out.write(StrUtils.decode_base64(response['Payload']['body']))
    elif output_type == OutputType.PLAIN_TEXT:
        output = text_message
        logger.info(output)
    else:
        if output_type == OutputType.JSON:
            output = json_output if json_output else {aws_output :
                                                      {'RequestId' : response['ResponseMetadata']['RequestId'],
                                                       'HTTPStatusCode' : response['ResponseMetadata']['HTTPStatusCode']}}
        elif output_type == OutputType.VERBOSE:
            output = verbose_output if verbose_output else {aws_output : response}
        logger.info_json(output)


def parse_lambda_function_creation_response(response, function_name, access_key, output_type):
    if response:
        aws_output = 'LambdaOutput'
        text_message = f"Function '{function_name}' successfully created."
        json_message = {aws_output : {'AccessKey' : access_key,
                                      'FunctionArn' : response['FunctionArn'],
                                      'Timeout' : response['Timeout'],
                                      'MemorySize' : response['MemorySize'],
                                      'FunctionName' : response['FunctionName']}}
        _print_generic_response(response, output_type, aws_output, text_message, json_output=json_message)


def parse_log_group_creation_response(response, log_group_name, output_type):
    if response:
        text_message = f"Log group '{log_group_name}' successfully created."
        _print_generic_response(response, output_type, 'CloudWatchOutput', text_message)


def parse_delete_function_response(response, function_name, output_type):
    if response:
        text_message = f"Function '{function_name}' successfully deleted."
        _print_generic_response(response, output_type, 'LambdaOutput', text_message)


def parse_delete_log_response(response, log_group_name, output_type):
    if response:
        text_message = f"Log group '{log_group_name}' successfully deleted."
        _print_generic_response(response, output_type, 'CloudWatchOutput', text_message)


def parse_delete_api_response(response, api_id, output_type):
    if response:
        text_message = f"API Endpoint '{api_id}' successfully deleted."
        _print_generic_response(response, output_type, 'APIGateway', text_message)


def parse_ls_response(lambda_functions, output_type):
    aws_output = 'Functions'
    result = []
    text_message = ""
    if output_type == OutputType.VERBOSE:
        result = lambda_functions
    else:
        for lambdaf in lambda_functions:
            result.append(_parse_lambda_function_info(lambdaf))
        text_message = _get_table(result)
    json_message = { aws_output : result }
    _print_generic_response('', output_type, aws_output, text_message, json_output=json_message, verbose_output=json_message)


def _parse_lambda_function_info(function_info):
    name = function_info.get('FunctionName', "-")
    memory = function_info.get('MemorySize', "-")
    timeout = function_info.get('Timeout', "-")
    image_id = function_info['Environment']['Variables'].get('IMAGE_ID', "-")
    api_gateway = function_info['Environment']['Variables'].get('API_GATEWAY_ID', "-")
    if api_gateway != '-':
        region = function_info['FunctionArn'].split(':')[3]
        api_gateway = f"https://{api_gateway}.execute-api.{region}.amazonaws.com/scar/launch"
    super_version = function_info.get('SupervisorVersion', '-')
    return {'Name' : name,
            'Memory' : memory,
            'Timeout' : timeout,
            'Image_id': image_id,
            'Api_gateway': api_gateway,
            'Sup_version': super_version}


def _get_table(functions_info):
    headers = ['NAME', 'MEMORY', 'TIME', 'IMAGE_ID', 'API_URL', 'SUPERVISOR_VERSION']
    table = []
    for function in functions_info:
        table.append([function['Name'],
                      function['Memory'],
                      function['Timeout'],
                      function['Image_id'],
                      function['Api_gateway'],
                      function['Sup_version']])
    return tabulate(table, headers)


def _parse_error_invocation_response(response, function_name):
    if response:
        if "Task timed out" in response['Payload']:
            # Find the timeout time
            message = StrUtils.find_expression(str(response['Payload']), '(Task timed out .* seconds)')
            # Modify the error message to ease the error readability
            error_msg = message.replace("Task", "Function '%s'" % function_name)
            error_log = f"Error in function response: {error_msg}"
        else:
            error_msg = "Error in function response."
            error_log = f"Error in function response: {response['Payload']}"
        logger.error(error_msg, error_log)


def _parse_payload(value):
    if 'Payload' in value and value['Payload']:
        payload = value['Payload'].read()
        if len(payload) > 0:
            value['Payload'] = json.loads(payload.decode("utf-8"))


def _parse_asynchronous_invocation_response(response, output_type, function_name):
    if response:
        aws_output = 'LambdaOutput'
        text_message = f"Request Id: {response['ResponseMetadata']['RequestId']}\n"
        text_message += f"Function '{function_name}' launched correctly"
        json_message = {aws_output : {'StatusCode' : response['StatusCode'],
                                       'RequestId' : response['ResponseMetadata']['RequestId']}}
        _print_generic_response(response, output_type, aws_output, text_message, json_output=json_message)


def _parse_requestresponse_invocation_response(**kwargs):
    if kwargs['Response']:
        response = kwargs['Response']
        aws_output = 'LambdaOutput'
        log_group_name = response['Payload']['headers']['amz-log-group-name']
        log_stream_name = response['Payload']['headers']['amz-log-stream-name']
        request_id = response['ResponseMetadata']['RequestId']
        if "exception" in response['Payload']['body']:
            body = ("ERROR launching udocker container: \n "
                    f"{json.loads(response['Payload']['body'])['exception']}")
        else:
            body = StrUtils.base64_to_utf8_string(response['Payload']['body'])

        text_message = (f"Request Id: {request_id}\n"
                        f"Log Group Name: {log_group_name}\n"
                        f"Log Stream Name: {log_stream_name}\n")
        text_message += body

        json_message = {aws_output : {'StatusCode' : response['StatusCode'],
                                      'Payload' : body,
                                      'LogGroupName' : log_group_name,
                                      'LogStreamName' : log_stream_name,
                                      'RequestId' : request_id}}
        if 'OutputFile' in kwargs and kwargs['OutputFile']:
            _print_generic_response(response, kwargs['OutputType'], aws_output, text_message, json_output=json_message, output_file=kwargs['OutputFile'])
        else:
            _print_generic_response(response, kwargs['OutputType'], aws_output, text_message, json_output=json_message)


def _parse_base64_response_values(value):
    value['LogResult'] = StrUtils.base64_to_utf8_string(value['LogResult'])
    value['ResponseMetadata']['HTTPHeaders']['x-amz-log-result'] = \
        StrUtils.base64_to_utf8_string(value['ResponseMetadata']['HTTPHeaders']['x-amz-log-result'])


def parse_invocation_response(**kwargs):
    # Decode and parse the payload
    _parse_payload(kwargs['Response'])
    if "FunctionError" in kwargs['Response']:
        _parse_error_invocation_response(kwargs['Response'], kwargs['FunctionName'])
    if kwargs['IsAsynchronous']:
        _parse_asynchronous_invocation_response(kwargs['Response'], kwargs['OutputType'], kwargs['FunctionName'])
    else:
        # Transform the base64 encoded results to something legible
        _parse_base64_response_values(kwargs['Response'])
        # Extract log_group_name and log_stream_name from the payload
        _parse_requestresponse_invocation_response(**kwargs)