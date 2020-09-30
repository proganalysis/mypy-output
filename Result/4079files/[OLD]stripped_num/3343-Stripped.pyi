# (generated with --quick)

from typing import Any, Type

CertificateStatus: Any
datetime: Type[datetime.datetime]
pytest: Any
test_parse_ocsp_request: Any
timedelta: Type[datetime.timedelta]
timezone: Type[datetime.timezone]

def test_build_ocsp_response(responder, ocsp_request_builder) -> None: ...
def test_get_cert_exception(responder, ocsp_request_builder) -> None: ...
def test_get_cert_invalid(responder, ocsp_request_builder) -> None: ...
def test_next_update_override(responder, ocsp_request_builder) -> None: ...
def test_nonce(responder, ocsp_request_builder) -> None: ...
def test_validate_noop(responder) -> None: ...
def test_verify_exception(responder, ocsp_request_builder) -> None: ...
def test_verify_good(responder, ocsp_request_builder) -> None: ...
def test_verify_revoked(responder, ocsp_request_builder) -> None: ...