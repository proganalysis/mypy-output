from typing import Any

def test_ignore_garbage(kresd_sock: Any, garbage_lengths: Any, single_buffer: Any, query_before: Any) -> None: ...
def test_pipelining(kresd_sock: Any) -> None: ...
def test_long_lived(kresd_sock: Any, duration: Any, delay: Any) -> None: ...
def test_close(kresd_sock: Any, query_before: Any) -> None: ...
def test_slow_lorris(kresd_sock: Any, query_before: Any) -> None: ...
def test_oob(kresd: Any, sock_func_name: Any) -> None: ...
def flood_buffer(msgcount: Any): ...
def test_query_flood_close(make_kresd_sock: Any) -> None: ...
def test_query_flood_no_recv(make_kresd_sock: Any) -> None: ...
def test_query_flood_garbage(make_kresd_silent_sock: Any, glength: Any, gcount: Any, delay: Any, query_before: Any) -> None: ...
