from ....typing import PartyID
from .models import Shop as DbShop
from .transfer.models import Shop, ShopID
from typing import List, Optional, Set

class UnknownShopId(ValueError): ...

def create_shop(party_id: PartyID) -> Shop: ...
def find_shop(shop_id: ShopID) -> Optional[Shop]: ...
def get_shop(shop_id: ShopID) -> Shop: ...
def find_shop_for_party(party_id: PartyID) -> Optional[Shop]: ...
def find_shops(shop_ids: Set[ShopID]) -> List[Shop]: ...
def get_active_shops() -> List[Shop]: ...
def _db_entity_to_shop(shop: DbShop) -> Shop: ...
