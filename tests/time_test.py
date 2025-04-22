import unittest
from datetime import datetime

from python.utils import is_chinese_workday, is_chinese_holiday

class TimeTest(unittest.TestCase):
    def test_time(self):
        holiday_dts = [
            datetime(2025, 1, 1),
            datetime(2025, 1, 28),
            datetime(2025, 2, 4),
            datetime(2025, 4, 4),
            datetime(2025, 5, 1),
            datetime(2025, 6, 2),
            datetime(2025, 10, 1),
            datetime(2025, 10, 8)
        ]
        workday_dts = [
            datetime(2025, 1, 26),
            datetime(2025, 2, 8),
            datetime(2025, 4, 27),
            datetime(2025, 9, 28),
            datetime(2025, 10, 11),
            datetime(2025, 4, 23)
        ]
        weekend_dts = [
            datetime(2025, 7, 27),
            datetime(2025, 5, 18),
            datetime(2025, 6, 15),
            datetime(2025, 8, 10),
        ]
        for dt in holiday_dts:
            self.assertTrue(is_chinese_holiday(dt), f"{dt} should be a holiday")
            self.assertFalse(is_chinese_workday(dt), f"{dt} should not be a workday")
        for dt in workday_dts:
            self.assertFalse(is_chinese_holiday(dt), f"{dt} should not be a holiday")
            self.assertTrue(is_chinese_workday(dt), f"{dt} should be a workday")
        for dt in weekend_dts:
            self.assertFalse(is_chinese_holiday(dt), f"{dt} should not be a holiday")
            self.assertFalse(is_chinese_workday(dt), f"{dt} should not be a workday")


if __name__ == '__main__':
    unittest.main()
