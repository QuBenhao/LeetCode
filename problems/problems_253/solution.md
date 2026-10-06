# [Python] Applying a difference array

> slug: python-chafenshuzu-by-himymben-9ekq
> date: 2022-04-02
> tags: Python, Python3
> question: Meeting Rooms II (meeting-rooms-ii)
> url: https://leetcode.cn/problems/meeting-rooms-ii/solutions/7AHRSa/python-chafenshuzu-by-himymben-9ekq/

---
### Approach
Use a difference array to find the maximum number of meeting rooms needed at any point in time.

### Code

```python3
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        diff = defaultdict(int)
        for start, end in intervals:
            diff[start] += 1
            diff[end] -= 1
        cur = ans = 0
        for _, v in sorted(diff.items()):
            cur += v
            ans = max(ans, cur)
        return ans
```
