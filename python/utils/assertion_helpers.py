"""Assertion helpers for LeetCode solution testing.

Extracted from test.py and tests.py to avoid code duplication.
"""

import unittest
from typing import Any, List, Optional, Tuple


def assert_result(
    test_case: unittest.TestCase,
    expected: Any,
    result: Any,
    problem_id: str = "",
    input_value: Any = None,
) -> None:
    """Assert that the result matches the expected output.

    Handles various output types including:
    - Float (with approximate comparison)
    - List (with nested list/set handling)
    - Set (checks if result is in expected set)
    - Simple equality

    Args:
        test_case: The unittest.TestCase instance
        expected: The expected output
        result: The actual result from solution
        problem_id: Problem ID for error messages
        input_value: Input value for error messages
    """
    msg_prefix = f"problem: {problem_id}, input = {input_value}" if problem_id else f"input = {input_value}"

    if expected is not None:
        test_case.assertIsNotNone(result, f"{msg_prefix}, No solution")

    if isinstance(expected, list):
        _assert_list_result(test_case, expected, result, msg_prefix)
    elif isinstance(result, list) and expected is not None:
        test_case.assertEqual(expected, result[0], msg=msg_prefix)
    else:
        _assert_scalar_result(test_case, expected, result, msg_prefix)


def _assert_list_result(
    test_case: unittest.TestCase,
    expected: List[Any],
    result: List[Any],
    msg_prefix: str,
) -> None:
    """Handle list type assertion with special cases."""
    if not expected:
        test_case.assertListEqual(expected, result, msg=msg_prefix)
        return

    if isinstance(expected[0], float):
        # Float comparison with delta
        for v1, v2 in zip(expected, result):
            test_case.assertAlmostEqual(v1, v2, msg=msg_prefix, delta=0.00001)
    elif (
        all(x is not None for x in expected)
        and (isinstance(expected[0], list) or isinstance(expected[0], set))
        and not any(None in x for x in expected)
    ):
        # Nested list/set - compare sorted
        try:
            test_case.assertListEqual(
                sorted(sorted(item) for item in expected),
                sorted(sorted(item) for item in result),
                msg=msg_prefix,
            )
        except TypeError:
            # Fallback for mixed types that can't be sorted
            test_case.assertListEqual(expected, result, msg=msg_prefix)
    else:
        test_case.assertListEqual(expected, result, msg=msg_prefix)


def _assert_scalar_result(
    test_case: unittest.TestCase,
    expected: Any,
    result: Any,
    msg_prefix: str,
) -> None:
    """Handle scalar type assertion with special cases."""
    if isinstance(expected, float):
        test_case.assertAlmostEqual(expected, result, msg=msg_prefix, delta=0.00001)
    elif isinstance(expected, set) and result and not isinstance(result, set):
        test_case.assertIn(result, expected, msg=msg_prefix)
    else:
        test_case.assertEqual(expected, result, msg=msg_prefix)


# Default max attempts for random output retry logic
# This value provides enough attempts (0.01% probability of missing a 1% chance)
# while keeping runtime reasonable
DEFAULT_MAX_RETRY_ATTEMPTS = 10002


def run_with_retry_on_random(
    solution_obj: Any,
    test_input: Any,
    expected: Any,
    max_attempts: int = DEFAULT_MAX_RETRY_ATTEMPTS,
) -> Tuple[Any, bool]:
    """Run solution with retry for random output scenarios.

    Some problems have non-deterministic outputs (e.g., random sampling).
    This function retries until the expected output is found or max attempts reached.

    Args:
        solution_obj: The Solution object with solve method
        test_input: The input to pass to solve
        expected: The expected output
        max_attempts: Maximum number of attempts (default 10002)

    Returns:
        Tuple of (final_result, success)
    """
    result = solution_obj.solve(test_input=test_input)

    for attempt in range(max_attempts - 1):
        try:
            if isinstance(expected, list):
                _compare_values(expected, result)
            else:
                _compare_values([expected], [result])
            return result, True
        except AssertionError:
            result = solution_obj.solve(test_input=test_input)

    return result, False


def _compare_values(expected: List[Any], result: List[Any], delta: float = 0.00001) -> None:
    """Compare values, raising AssertionError if not equal.

    Handles float comparison with delta tolerance for floating point precision.

    Args:
        expected: Expected values
        result: Actual values
        delta: Tolerance for float comparison
    """
    if len(expected) != len(result):
        raise AssertionError(f"Length mismatch: {len(expected)} vs {len(result)}")
    for e, r in zip(expected, result):
        # Handle float comparison with delta
        if isinstance(e, float) and isinstance(r, float):
            if abs(e - r) > delta:
                raise AssertionError(f"Float value mismatch: {e} vs {r} (delta={delta})")
        elif e != r:
            raise AssertionError(f"Value mismatch: {e} vs {r}")
