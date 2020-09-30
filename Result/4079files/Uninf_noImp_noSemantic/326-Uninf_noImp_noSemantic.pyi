from default_imports import *
from modules.auth.Priv import Priv
from modules.auth.Token import Token, TokenID
from modules.auth.User import Password, User, UserID, Username
from typing import Any, TypeVar

Authable = TypeVar('Authable', User, Token)
Authorised: Any
AuthID = TypeVar('AuthID', UserID, TokenID)

class Auth:
    def loginUser(self, username: Username, password: Password) -> Tuple[Opt[User], Authorised]: ...
    def registerUser(self, name: Username, password: Password, privs: List[Priv]=...) -> Opt[User]: ...
    def authoriseTokenId(self, tokenId: TokenID, priv: Priv) -> Tuple[Opt[Token], Authorised]: ...
    def authoriseUser(self, username: Username, password: Password, priv: Priv) -> Tuple[Opt[User], Authorised]: ...
    def authoriseRequest(self, req: Opt[Dict], priv: Priv) -> Tuple[Opt[Authable], Authorised]: ...
    def authoriseRoute(self, priv: Priv) -> Any: ...
