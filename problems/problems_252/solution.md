# [Python] 按会议开始时间排序

> slug: python-an-hui-yi-kai-shi-shi-jian-pai-xu-0ncf
> date: 2021-08-22
> tags: Python, Python3
> question: Meeting Rooms (meeting-rooms)
> url: https://leetcode.cn/problems/meeting-rooms/solutions/qLyuUe/python-an-hui-yi-kai-shi-shi-jian-pai-xu-0ncf/

---
### 解题思路
如果上一个会议先开始了，而且下一个会议开始了它还没结束，就不行

### 代码

```python3
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # 根据会议开始时间排序
        intervals.sort(key=lambda x:x[0])
        return all(intervals[i-1][1] <= intervals[i][0] for i in range(1, len(intervals)))

```