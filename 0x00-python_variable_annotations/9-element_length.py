#!/usr/bin/env python3
'''Module for Task 9
'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Returns a list of tuples containing the element and its length.
    '''
    return [(element, len(element)) for element in lst]
