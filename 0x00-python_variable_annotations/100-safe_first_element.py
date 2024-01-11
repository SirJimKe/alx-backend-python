#!/usr/bin/env python3
"""Duck-typed annotations"""


from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a list, or None if the list is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
