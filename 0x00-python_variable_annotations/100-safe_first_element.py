#!/usr/bin/env python3
"""Duck-typed annotations"""


from typing import Any, List, Optional


def safe_first_element(lst: List[Any]) -> Optional[Any]:
    """
    Returns the first element of a list, or None if the list is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
