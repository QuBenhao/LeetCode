# [Python] Learn from the official solution to handle times in the same 15-minute interval

> Author: Benhao
> Date: 2021-06-20
> Upvotes: 1
> Tags: Python, Python3

---

### Approach
Count complete 15-minute intervals by converting both times to minutes.
Handle times in the same 15-minute interval, such as ["12:01", "12:02"].

### Code

```python3
class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        # Count complete quarter-hours between s and f; 01->29 does not contain one
        start = int(startTime[:2]) * 60 + int(startTime[3:])
        finish = int(finishTime[:2]) * 60 + int(finishTime[3:])
        # Overnight case
        if finish < start:
            # Add one day
            finish += 24 * 60
        # The finish must fall on a quarter-hour boundary
        finish = finish // 15 * 15
        # No need to adjust the start to a boundary here, since floor division by 15 gives the same result
        return (finish - start) // 15 if finish > start else 0

```
