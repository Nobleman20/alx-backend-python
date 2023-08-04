#!/usr/bin/env python3
'''Module for Task 11
'''
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    '''Returns the value with the given key in the dictionary
    '''
    return dct.get(key, default)
