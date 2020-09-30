# (generated with --quick)

import configmaster.ConfigFile
import configmaster.ConfigKey
import requests.models
from typing import Any, Type

ConfigKey: Type[configmaster.ConfigKey.ConfigKey]
INIConfigFile: configmaster.ConfigFile.ConfigFile
JSONConfigFile: configmaster.ConfigFile.ConfigFile
NetworkedJSONConfigFile: configmaster.ConfigFile.NetworkedConfigObject
YAMLConfigFile: configmaster.ConfigFile.ConfigFile
__has_requests: bool
__has_yaml: bool
__site_up: bool
exc: Any
os: module
pytest: Any
r: requests.models.Response
requests: module
test_invalid_json_data: Any
test_invalid_key_get: Any
test_invalid_yaml_data: Any
test_loading_valid_yml: Any
test_network_json_bad_data: Any
test_network_json_dump: Any
test_network_json_get_bad_url: Any
test_network_json_get_unsafe_data: Any
test_network_json_get_url: Any
test_network_json_populate: Any

def test_configkey_dump() -> None: ...
def test_configkey_iter() -> None: ...
def test_created_config_file() -> None: ...
def test_dumpd() -> None: ...
def test_dumps() -> None: ...
def test_embedded_dict() -> None: ...
def test_embedded_dict_getitem() -> None: ...
def test_embedded_dict_inside_list() -> None: ...
def test_embedded_list() -> None: ...
def test_initial_populate() -> None: ...
def test_loaded_config_item() -> None: ...
def test_loading_valid_ini() -> None: ...
def test_loading_valid_json() -> None: ...
def test_unsafe_load() -> None: ...
