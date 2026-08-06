# [Python] 差分数组应用

> slug: python-chafenshuzu-by-himymben-9ekq
> date: 2022-04-02
> tags: Python, Python3
> question: Meeting Rooms II (meeting-rooms-ii)
> url: https://leetcode.cn/problems/meeting-rooms-ii/solutions/7AHRSa/python-chafenshuzu-by-himymben-9ekq/

---
### 解题思路
求某一时刻所需会议室的最大值，可以用差分来做

### 代码

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