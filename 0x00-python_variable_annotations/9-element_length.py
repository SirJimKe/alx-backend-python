#!/usr/bin/env python3
"""Duck type iterable"""


from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Returns a list of tuples, where each tuple contains an
    element from the input list and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
