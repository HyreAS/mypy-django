# Stubs for django.utils.six (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import types
from typing import Any, Optional

PY2: Any
PY3: Any
PY34: Any
string_types: Any
integer_types: Any
class_types: Any
text_type = str
binary_type = bytes
MAXSIZE: Any
text_type = unicode
binary_type = str

class X:
    def __len__(self): ...

class _LazyDescr:
    name: Any = ...
    def __init__(self, name) -> None: ...
    def __get__(self, obj, tp): ...

class MovedModule(_LazyDescr):
    mod: Any = ...
    def __init__(self, name, old, new: Optional[Any] = ...) -> None: ...
    def __getattr__(self, attr): ...

class _LazyModule(types.ModuleType):
    __doc__: Any = ...
    def __init__(self, name) -> None: ...
    def __dir__(self): ...

class MovedAttribute(_LazyDescr):
    mod: Any = ...
    attr: Any = ...
    def __init__(self, name, old_mod, new_mod, old_attr: Optional[Any] = ..., new_attr: Optional[Any] = ...) -> None: ...

class _SixMetaPathImporter:
    name: Any = ...
    known_modules: Any = ...
    def __init__(self, six_module_name) -> None: ...
    def find_module(self, fullname, path: Optional[Any] = ...): ...
    def load_module(self, fullname): ...
    def is_package(self, fullname): ...
    def get_code(self, fullname): ...
    get_source: Any = ...

class _MovedItems(_LazyModule):
    __path__: Any = ...

moves: Any

class Module_six_moves_urllib_parse(_LazyModule): ...
class Module_six_moves_urllib_error(_LazyModule): ...
class Module_six_moves_urllib_request(_LazyModule): ...
class Module_six_moves_urllib_response(_LazyModule): ...
class Module_six_moves_urllib_robotparser(_LazyModule): ...

class Module_six_moves_urllib(types.ModuleType):
    __path__: Any = ...
    parse: Any = ...
    error: Any = ...
    request: Any = ...
    response: Any = ...
    robotparser: Any = ...
    def __dir__(self): ...

def add_move(move): ...
def remove_move(name): ...
advance_iterator = next
next = advance_iterator
callable = callable

def get_unbound_function(unbound): ...

create_bound_method: Any

def create_unbound_method(func, cls): ...
Iterator = object

class Iterator:
    def next(self): ...
callable = callable
get_method_function: Any
get_method_self: Any
get_function_closure: Any
get_function_code: Any
get_function_defaults: Any
get_function_globals: Any

def iterkeys(d, **kw): ...
def itervalues(d, **kw): ...
def iteritems(d, **kw): ...
def iterlists(d, **kw): ...

viewkeys: Any
viewvalues: Any
viewitems: Any

def b(s): ...
def u(s): ...
unichr = chr
int2byte: Any
byte2int: Any
indexbytes: Any
iterbytes = iter
StringIO: Any
BytesIO: Any
unichr = unichr
int2byte = chr

def assertCountEqual(self, *args, **kwargs): ...
def assertRaisesRegex(self, *args, **kwargs): ...
def assertRegex(self, *args, **kwargs): ...

exec_: Any

def reraise(tp, value, tb: Optional[Any] = ...): ...
def raise_from(value, from_value): ...

print_: Any
_print = print_

def wraps(wrapped, assigned: Any = ..., updated: Any = ...): ...

wraps: Any

def with_metaclass(meta, *bases): ...
def add_metaclass(metaclass): ...
def python_2_unicode_compatible(klass): ...

__path__: Any
__package__ = __name__
memoryview = memoryview
buffer_types: Any
memoryview = memoryview
memoryview = buffer