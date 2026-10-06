# [Python] Sort by meeting start time

> slug: python-an-hui-yi-kai-shi-shi-jian-pai-xu-0ncf
> date: 2021-08-22
> tags: Python, Python3
> question: Meeting Rooms (meeting-rooms)
> url: https://leetcode.cn/problems/meeting-rooms/solutions/qLyuUe/python-an-hui-yi-kai-shi-shi-jian-pai-xu-0ncf/

---
### Approach
If one meeting starts earlier and has not ended when the next meeting starts, the schedule is invalid.

### Code

```python3
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Sort by meeting start time
        intervals.sort(key=lambda x:x[0])
        return all(intervals[i-1][1] <= intervals[i][0] for i in range(1, len(intervals)))

```
