#!/usr/bin/env python3
'''Task 12's module
'''
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    '''Expands a tuple by duplicating each element multiple times.
    '''
    zoomed_lst: List = [item for item in lst for _ in range(factor)]
    return zoomed_lst


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, factor=3)
