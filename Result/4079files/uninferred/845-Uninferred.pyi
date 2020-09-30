from enum import Enum
from graphql import GraphQLObjectType, GraphQLSchema
from typing import Any, Callable

pytestmark: Any

class EnumTest(Enum):
    VALUE_ONE: str = ...
    VALUE_TWO: str = ...

def define_schema(resolver: Callable, enumType: GraphQLObjectType) -> GraphQLSchema: ...

GraphQLEnumTest: Any

async def test_out_enum() -> None: ...
async def test_enum_args() -> None: ...
