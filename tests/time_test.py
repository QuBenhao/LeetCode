"""Tests for time utility functions."""

import pytest
from datetime import datetime

from python.utils import is_chinese_workday, is_chinese_holiday


@pytest.mark.unit
class TestTimeUtils:
    """Unit tests for time-related utilities."""

    @pytest.fixture
    def holiday_dates(self):
        """Chinese holidays in 2025."""
        return [
            datetime(2025, 1, 1),
            datetime(2025, 1, 28),
            datetime(2025, 2, 4),
            datetime(2025, 4, 4),
            datetime(2025, 5, 1),
            datetime(2025, 6, 2),
            datetime(2025, 10, 1),
            datetime(2025, 10, 8)
        ]

    @pytest.fixture
    def workday_dates(self):
        """Chinese workdays (weekend makeup days) in 2025."""
        return [
            datetime(2025, 1, 26),
            datetime(2025, 2, 8),
            datetime(2025, 4, 27),
            datetime(2025, 9, 28),
            datetime(2025, 10, 11),
            datetime(2025, 4, 23)
        ]

    @pytest.fixture
    def weekend_dates(self):
        """Regular weekend dates."""
        return [
            datetime(2025, 7, 27),
            datetime(2025, 5, 18),
            datetime(2025, 6, 15),
            datetime(2025, 8, 10),
        ]

    def test_holidays_detected(self, holiday_dates):
        """Test that holidays are correctly identified."""
        for dt in holiday_dates:
            assert is_chinese_holiday(dt), f"{dt} should be a holiday"
            assert not is_chinese_workday(dt), f"{dt} should not be a workday"

    def test_workdays_detected(self, workday_dates):
        """Test that makeup workdays are correctly identified."""
        for dt in workday_dates:
            assert not is_chinese_holiday(dt), f"{dt} should not be a holiday"
            assert is_chinese_workday(dt), f"{dt} should be a workday"

    def test_weekends_detected(self, weekend_dates):
        """Test that regular weekends are correctly identified."""
        for dt in weekend_dates:
            assert not is_chinese_holiday(dt), f"{dt} should not be a holiday"
            assert not is_chinese_workday(dt), f"{dt} should not be a workday"
