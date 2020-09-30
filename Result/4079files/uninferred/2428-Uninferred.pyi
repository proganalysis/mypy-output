from typing import Any

def parse_data(data: Any): ...
def parse_date_element(el: Any): ...

class Resource:
    resource: Any = ...
    def __init__(self) -> None: ...
    @property
    def resource_id(self): ...

class Division(Resource):
    house: Any = ...
    parl: Any = ...
    _data_fetched: bool = ...
    title: Any = ...
    uin: Any = ...
    date: Any = ...
    def __init__(self, house: Any) -> None: ...
    abstain: Any = ...
    ayes: Any = ...
    did_not_vote: Any = ...
    error_vote: Any = ...
    margin: Any = ...
    noes: Any = ...
    non_eligible: Any = ...
    suspended_expelled: Any = ...
    votes: Any = ...
    contents: Any = ...
    not_contents: Any = ...
    def _fetch_data(self) -> None: ...
    @property
    def passed(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __repr__(self): ...
    def __getattr__(self, name: str) -> Any: ...

class EDM(Resource):
    def __repr__(self): ...

class Bill(Resource):
    parl: Any = ...
    title: Any = ...
    home_page: Any = ...
    type: Any = ...
    date: Any = ...
    def __init__(self, parl: Any) -> None: ...
    description: Any = ...
    def fetch_data(self) -> None: ...
    def __repr__(self): ...

class Member(Resource):
    house: Any = ...
    id: Any = ...
    parl: Any = ...
    display_name: Any = ...
    party: Any = ...
    _data_fetched: bool = ...
    def __init__(self, parl: Any, house: Any, member_id: Any) -> None: ...
    def _fetch_data(self) -> None: ...
    dods_id: Any = ...
    pims_id: Any = ...
    full_name: Any = ...
    date_of_birth: Any = ...
    start_date: Any = ...
    end_date: Any = ...
    gender: Any = ...
    constituency: Any = ...
    member_type: Any = ...
    def _populate_data(self, data: Any) -> None: ...
    def __repr__(self): ...
    def __getattr__(self, name: str) -> Any: ...

class MemberList(list):
    def by_party(self): ...
