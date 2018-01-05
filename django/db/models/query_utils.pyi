# Stubs for django.db.models.query_utils (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from collections import namedtuple
from django.utils import tree
from typing import Any, Optional

PathInfo = namedtuple('PathInfo', 'from_opts to_opts target_fields join_field m2m direct')

class InvalidQuery(Exception): ...

def subclasses(cls): ...

class QueryWrapper:
    contains_aggregate: bool = ...
    data: Any = ...
    def __init__(self, sql, params) -> None: ...
    def as_sql(self, compiler: Optional[Any] = ..., connection: Optional[Any] = ...): ...

class Q(tree.Node):
    AND: str = ...
    OR: str = ...
    default: Any = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __or__(self, other): ...
    def __and__(self, other): ...
    def __invert__(self): ...
    def resolve_expression(self, query: Optional[Any] = ..., allow_joins: bool = ..., reuse: Optional[Any] = ..., summarize: bool = ..., for_save: bool = ...): ...

class DeferredAttribute:
    field_name: Any = ...
    def __init__(self, field_name, model) -> None: ...
    def __get__(self, instance, cls: Optional[Any] = ...): ...

class RegisterLookupMixin:
    @classmethod
    def get_lookups(cls): ...
    def get_lookup(self, lookup_name): ...
    def get_transform(self, lookup_name): ...
    @staticmethod
    def merge_dicts(dicts): ...
    @classmethod
    def register_lookup(cls, lookup, lookup_name: Optional[Any] = ...): ...

def select_related_descend(field, restricted, requested, load_fields, reverse: bool = ...): ...
def refs_expression(lookup_parts, annotations): ...
def check_rel_lookup_compatibility(model, target_opts, field): ...
