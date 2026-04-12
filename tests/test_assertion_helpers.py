"""Unit tests for assertion_helpers module."""

import pytest
from typing import Any, List

from python.utils.assertion_helpers import (
    assert_result,
    run_with_retry_on_random,
    _compare_values,
    DEFAULT_MAX_RETRY_ATTEMPTS,
)


class MockTestCase:
    """Mock test case for testing assertion helpers - NOT a unittest.TestCase."""

    def __init__(self):
        self.assertions_passed = 0
        self.last_error = None

    def assertAlmostEqual(self, a, b, msg=None, delta=0.00001):
        if abs(a - b) > delta:
            raise AssertionError(f"Values not close: {a} vs {b}")
        self.assertions_passed += 1

    def assertEqual(self, a, b, msg=None):
        if a != b:
            raise AssertionError(f"Values not equal: {a} vs {b}")
        self.assertions_passed += 1

    def assertListEqual(self, a, b, msg=None):
        if a != b:
            raise AssertionError(f"Lists not equal: {a} vs {b}")
        self.assertions_passed += 1

    def assertIn(self, item, container, msg=None):
        if item not in container:
            raise AssertionError(f"Item {item} not in {container}")
        self.assertions_passed += 1

    def assertIsNotNone(self, obj, msg=None):
        if obj is None:
            raise AssertionError("Object is None")
        self.assertions_passed += 1


@pytest.fixture
def mock_test_case():
    """Provide a mock test case instance."""
    return MockTestCase()


@pytest.mark.unit
class TestAssertResult:
    """Tests for assert_result function."""

    def test_simple_integer(self, mock_test_case):
        """Test assertion with simple integer values."""
        assert_result(mock_test_case, 42, 42, problem_id="1", input_value=[1, 2])
        assert mock_test_case.assertions_passed >= 1

    def test_simple_string(self, mock_test_case):
        """Test assertion with string values."""
        assert_result(mock_test_case, "hello", "hello")
        assert mock_test_case.assertions_passed >= 1

    def test_float_values(self, mock_test_case):
        """Test assertion with floating point values."""
        assert_result(mock_test_case, 3.14159, 3.14159)
        assert mock_test_case.assertions_passed >= 1

    def test_float_with_delta(self, mock_test_case):
        """Test float comparison uses delta."""
        assert_result(mock_test_case, 0.1 + 0.2, 0.3)
        assert mock_test_case.assertions_passed >= 1

    def test_list_of_integers(self, mock_test_case):
        """Test assertion with list of integers."""
        assert_result(mock_test_case, [1, 2, 3], [1, 2, 3])
        assert mock_test_case.assertions_passed >= 1

    def test_list_of_floats(self, mock_test_case):
        """Test assertion with list of floats."""
        assert_result(mock_test_case, [0.1, 0.2, 0.3], [0.1, 0.2, 0.3])
        assert mock_test_case.assertions_passed >= 3

    def test_nested_lists(self, mock_test_case):
        """Test assertion with nested lists."""
        assert_result(mock_test_case, [[1, 2], [3, 4]], [[1, 2], [3, 4]])
        assert mock_test_case.assertions_passed >= 1

    def test_set_membership(self, mock_test_case):
        """Test assertion when expected is a set."""
        assert_result(mock_test_case, {1, 2, 3}, 2)
        assert mock_test_case.assertions_passed >= 1

    def test_none_expected(self, mock_test_case):
        """Test assertion with None expected value."""
        assert_result(mock_test_case, None, None)
        # No assertion should be made when expected is None


@pytest.mark.unit
class TestRunWithRetry:
    """Tests for run_with_retry_on_random function."""

    def test_immediate_success(self):
        """Test when result matches immediately."""
        class MockSolution:
            def solve(self, test_input):
                return [1, 2, 3]

        result, success = run_with_retry_on_random(MockSolution(), "input", [1, 2, 3], max_attempts=10)
        assert success is True
        assert result == [1, 2, 3]

    def test_never_success(self):
        """Test when result never matches."""
        class MockSolution:
            call_count = 0

            def solve(self, test_input):
                MockSolution.call_count += 1
                return [MockSolution.call_count]

        result, success = run_with_retry_on_random(MockSolution(), "input", [100], max_attempts=5)
        assert success is False
        # After max_attempts, the last result is returned
        assert result[0] == MockSolution.call_count

    def test_eventual_success(self):
        """Test when result matches after several attempts."""
        class MockSolution:
            call_count = 0

            def solve(self, test_input):
                self.call_count += 1
                if self.call_count >= 3:
                    return [1, 2, 3]
                return [0, 0, 0]

        result, success = run_with_retry_on_random(MockSolution(), "input", [1, 2, 3], max_attempts=10)
        assert success is True
        assert result == [1, 2, 3]

    def test_default_max_attempts_constant(self):
        """Test that DEFAULT_MAX_RETRY_ATTEMPTS is defined and reasonable."""
        # Should be a positive integer
        assert isinstance(DEFAULT_MAX_RETRY_ATTEMPTS, int)
        assert DEFAULT_MAX_RETRY_ATTEMPTS > 0
        # Should be large enough for random probability cases
        # (0.01% probability of missing a 1% chance)
        assert DEFAULT_MAX_RETRY_ATTEMPTS >= 1000


@pytest.mark.unit
class TestCompareValues:
    """Tests for _compare_values function."""

    def test_equal_lists(self):
        """Test comparison of equal lists."""
        _compare_values([1, 2, 3], [1, 2, 3])

    def test_unequal_lists(self):
        """Test comparison of unequal lists."""
        with pytest.raises(AssertionError):
            _compare_values([1, 2, 3], [1, 2, 4])

    def test_different_length(self):
        """Test comparison of different length lists."""
        with pytest.raises(AssertionError):
            _compare_values([1, 2, 3], [1, 2])

    def test_float_with_delta(self):
        """Test float comparison uses delta tolerance."""
        # 0.1 + 0.2 = 0.30000000000000004 in floating point
        _compare_values([0.1 + 0.2], [0.3])

    def test_float_exact_match(self):
        """Test exact float match."""
        _compare_values([3.14159], [3.14159])

    def test_float_outside_delta(self):
        """Test float comparison fails when outside delta."""
        with pytest.raises(AssertionError, match="Float value mismatch"):
            _compare_values([1.0], [2.0])

    def test_float_custom_delta(self):
        """Test float comparison with custom delta."""
        # Default delta is 0.00001, but we use larger values
        _compare_values([1.0, 1.1], [1.0, 1.1], delta=0.5)  # Should pass
        with pytest.raises(AssertionError):
            _compare_values([1.0], [2.0], delta=0.5)

    def test_mixed_types(self):
        """Test comparison with mixed int and float."""
        _compare_values([1, 2.0, 3], [1, 2.0, 3])