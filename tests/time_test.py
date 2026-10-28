"""Tests for time utility functions."""

import json
import os
import time
from datetime import datetime, timedelta, timezone

import pytest

from python.lc_libs import study_plan
from python.utils import is_chinese_workday, is_chinese_holiday
from python.utils import time_util


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

    @staticmethod
    def _china_epoch(dt: datetime) -> float:
        """Epoch seconds for a China (UTC+8) wall-clock time."""
        return dt.replace(tzinfo=timezone(timedelta(hours=8))).timestamp()

    @pytest.mark.skipif(not hasattr(time, "tzset"), reason="tzset is not available")
    def test_china_daily_time_independent_of_host_timezone(self, monkeypatch):
        # China 2026-10-25 21:00: the moment a +3 host is most likely to shift the date.
        fixed_epoch = self._china_epoch(datetime(2026, 10, 25, 21))
        monkeypatch.setattr(time_util.time, "time", lambda: fixed_epoch)
        expected = self._china_epoch(datetime(2026, 10, 25, 0))

        original_tz = os.environ.get("TZ")
        try:
            for host_tz in ("UTC", "Europe/Istanbul", "Asia/Shanghai", "America/Los_Angeles"):
                os.environ["TZ"] = host_tz
                time.tzset()
                assert int(time_util.get_china_daily_time()) == int(expected)
        finally:
            if original_tz is None:
                os.environ.pop("TZ", None)
            else:
                os.environ["TZ"] = original_tz
            time.tzset()

    @pytest.mark.skipif(not hasattr(time, "tzset"), reason="tzset is not available")
    @pytest.mark.parametrize("china_wall_clock, expected_todo_num", [
        (datetime(2026, 10, 25, 21), 2),   # Sunday evening in China
        (datetime(2026, 10, 26, 10), 1),   # Monday workday
        (datetime(2026, 10, 1, 10), 0),    # National Day holiday
        (datetime(2026, 10, 10, 10), 1),   # Saturday makeup workday
    ])
    def test_study_plan_todo_num_follows_china_date(self, monkeypatch, china_wall_clock, expected_todo_num):
        monkeypatch.setattr(time_util.time, "time", lambda: self._china_epoch(china_wall_clock))
        captured = {}

        def fake_generate(_groups, todo_num):
            captured["todo_num"] = todo_num
            return set(), set(), []

        monkeypatch.setattr(study_plan, "generate_question_todo", fake_generate)

        payload = {"data": {"studyPlanV2ProgressDetail": {
            "status": "ON_GOING",
            "finishedQuestionNum": 1,
            "studyPlanDetail": {"questionNum": 5, "planSubGroups": []},
        }}}

        class _FakeResponse:
            def __init__(self, text):
                self.text = text

        def fake_request(_backend, handler, **_kwargs):
            return handler(_FakeResponse(json.dumps(payload)))

        monkeypatch.setattr(study_plan, "general_request", fake_request)

        original_tz = os.environ.get("TZ")
        try:
            # A +3 host must not shift the China "today" used for holiday checks.
            os.environ["TZ"] = "Europe/Istanbul"
            time.tzset()
            result = study_plan.get_user_study_plan_progress("plan", "cookie")
        finally:
            if original_tz is None:
                os.environ.pop("TZ", None)
            else:
                os.environ["TZ"] = original_tz
            time.tzset()

        assert result == {
            "total": 5,
            "finished": 1,
            "all_problems": set(),
            "all_solved": set(),
            "recommend": [],
        }
        assert captured["todo_num"] == expected_todo_num
