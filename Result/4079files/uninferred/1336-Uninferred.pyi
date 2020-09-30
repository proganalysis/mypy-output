from typing import Any

def owner_check(ctx: Any): ...
async def role_check(ctx: Any, _role: Any): ...
def permission_check(ctx: Any, **permission_pairs: Any): ...
def is_owner(): ...
def is_bot_account(): ...
def is_not_bot_account(): ...
def is_selfbot(): ...
def is_not_selfbot(): ...
def is_main_shard(): ...
def is_not_main_shard(): ...
def mod_or_permissions(**permissions: Any): ...
def admin_or_permissions(**permissions: Any): ...
def serverowner_or_permissions(**permissions: Any): ...
serverowner = serverowner_or_permissions
admin = admin_or_permissions
mod = mod_or_permissions
