# (generated with --quick)

from typing import Any, NoReturn, Union
import werkzeug.wrappers

re: module

def abort(status: Union[int, werkzeug.wrappers.Response], *args, **kwargs) -> NoReturn: ...
def format_framework_integrity_error_message(error, json_framework) -> str: ...
def get_validation_errors(validator_name, json_data, enforce_required = ..., required_fields = ...) -> Any: ...
def validate_framework_agreement_details_data(framework_agreement_details, enforce_required = ..., required_fields = ...) -> None: ...