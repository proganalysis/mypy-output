from typing import Any

class MovieInfo:
    id: str = ...
    name: Any = ...
    release_date: Any = ...
    is_imax: Any = ...
    def __init__(self, movie_code: Any, name: Any, release_date: Any, is_imax: Any) -> None: ...
    def __repr__(self) -> str: ...

MOVIE_INFO_CACHE: Any

def is_imax_movie(movie_code: Any): ...
def get_movie_info(movie_code: Any): ...
def save_movie_info(movie_info: Any) -> None: ...

logger: Any
