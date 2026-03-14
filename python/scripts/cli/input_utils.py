"""
Input utilities for LeetCode CLI
Provides functions for validated user input.
"""

import random
import re
import sys
from typing import Callable, List, Optional, Any

SEPARATE_LINE = "-" * 50


def input_until_valid(prompt: str,
                      check_func: Callable[[str], bool],
                      error_msg: Optional[str] = None) -> str:
    """
    Keep prompting user until valid input is received.

    Args:
        prompt: The prompt to display to the user
        check_func: A function that returns True if input is valid
        error_msg: Optional error message to display on invalid input

    Returns:
        The valid user input
    """
    while True:
        try:
            user_input = input(prompt)
            if check_func(user_input):
                return user_input
            elif error_msg:
                print(error_msg)
            print(SEPARATE_LINE)
        except EOFError:
            # Handle pipe input end
            sys.exit(0)


def input_pick_array(desc: str, arr: List[Any]) -> Optional[int]:
    """
    Let user pick an item from an array.

    Args:
        desc: Description of what to pick
        arr: List of items to choose from

    Returns:
        Index of selected item, or None if user chose to go back
    """
    user_input = input_until_valid(
        f"Enter the number of the {desc} [1-{len(arr)}, or 0 to go back (default), or input random to random:\n"
        f"0. Back\n{'\n'.join(f'{i}. {v}' for i, v in enumerate(arr, 1))}\n",
        lambda x: True  # Allow any input
    )
    if user_input == "0":
        return None
    if user_input == "random":
        return random.randint(0, len(arr) - 1)
    try:
        pick = int(user_input) - 1
        if pick < 0 or pick >= len(arr):
            pick = random.randint(0, len(arr) - 1)
        return pick
    except ValueError:
        return None


# Common validation functions
def allow_all(_: str) -> bool:
    """Accept any input."""
    return True


def allow_all_not_empty(x: str) -> bool:
    """Accept any non-empty input."""
    return bool(x.strip())


def allow_number(x: str) -> bool:
    """Accept only numeric input."""
    return bool(re.match(r"^\d+$", x))
