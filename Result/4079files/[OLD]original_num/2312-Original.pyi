# (generated with --quick)

from typing import Any, Optional, Tuple

DEFAULT_TTL: int
DNSException: Any
SyntaxError: Any
dns: Any
log: logging.Logger
logging: module
re: module
socket: module

class DDNSUpdater:
    __doc__: str
    algo: Optional[str]
    domain: Any
    keyfile: Any
    keyring: Any
    server: Any
    ttl: Any
    def __init__(self, server, keyfile, domain, ttl = ...) -> None: ...
    def _add_ptr(self, fqdn, ip) -> None: ...
    def _add_record(self, qtype, fqdn, ip, do_ptr) -> None: ...
    def _del_ptr(self, fqdn, ip) -> None: ...
    def _delete_record(self, qtype, fqdn, data, do_ptr) -> None: ...
    def _do_update(self, update) -> None: ...
    def _get_fqdn(self, hostname) -> Any: ...
    def _is_valid_name(self, name) -> bool: ...
    def _is_valid_v4addr(self, address) -> bool: ...
    def _is_valid_v6addr(self, address) -> bool: ...
    def _parse_name(self, name) -> Tuple[Any, Any]: ...
    def _prep_ptr(self, ip) -> Tuple[Any, Any]: ...
    def _read_key(self) -> None: ...
    def _update_ptr(self, fqdn, ip) -> None: ...
    def _update_record(self, qtype, fqdn, data, do_ptr) -> None: ...
    def add_a_record(self, hostname, ip, do_ptr = ...) -> None: ...
    def add_aaaa_record(self, hostname, ip, do_ptr = ...) -> None: ...
    def delete_a_record(self, hostname, ip, do_ptr = ...) -> None: ...
