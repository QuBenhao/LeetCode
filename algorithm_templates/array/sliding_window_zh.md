# 滑动窗口

```python3
def max_sliding_window(nums, k):
    from collections import deque
    q = deque()
    res = []
    for i in range(len(nums)):
        if q and q[0] < i - k + 1:
            q.popleft()
        while q and nums[q[-1]] < nums[i]:
            q.pop()
        q.append(i)
        if i >= k - 1:
            res.append(nums[q[0]])
    return res
```

```go
package main

func maxSlidingWindow(nums []int, k int) (ans []int) {
    q := make([]int, 0)
    for i := range nums {
        if len(q) > 0 && q[0] < i-k+1 {
            q = q[1:]
        }
        for len(q) > 0 && nums[q[len(q)-1]] < nums[i] {
            q = q[:len(q)-1]
        }
        q = append(q, i)
        if i >= k-1 {
            ans = append(ans, nums[q[0]])
        }
    }
    return
}
```