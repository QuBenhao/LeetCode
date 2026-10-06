# [Python/Go] Greedy dynamic programming o(n)

> slug: pythongo-tan-xin-dong-tai-gui-hua-on-by-mbqmm
> date: 2022-02-24
> tags: Go, Python, Python3
> question: Wiggle Subsequence (wiggle-subsequence)
> url: https://leetcode.cn/problems/wiggle-subsequence/solutions/FSOdMG/pythongo-tan-xin-dong-tai-gui-hua-on-by-mbqmm/

---
### Approach
Maintain a longest wiggle subsequence.

Greedily choose the minimum of each descending run and the maximum of each ascending run. For example, an ascending run contributes at most two values to an upward wiggle, and taking the largest value makes the next downward wiggle easier.

An advantage is that this approach can return the longest wiggle subsequence itself if required.

### Code

```Python3 []
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        ans = []
        for num in nums:
            if len(ans) > 1:
                # An upward wiggle is next
                if ans[-2] > ans[-1]:
                    if num > ans[-1]:
                        ans.append(num)
                    else:
                        ans[-1] = num
                # A downward wiggle is next
                else:
                    if num < ans[-1]:
                        ans.append(num)
                    else:
                        ans[-1] = num
            elif not ans or ans[-1] != num:
                ans.append(num)
        return len(ans)
```
```Go []
func wiggleMaxLength(nums []int) int {
    ans := []int{}
    for _, num := range nums {
        if v := len(ans); v > 1 {
            if ans[v - 2] > ans[v - 1] {
                if num > ans[v - 1] {
                    ans = append(ans, num)
                } else {
                    ans[v - 1] = num
                }
            } else {
                if num < ans[v - 1] {
                    ans = append(ans, num)
                } else {
                    ans[v - 1] = num
                }
            }
        } else if v == 0 || ans[v - 1] != num {
            ans = append(ans, num)
        }
    }
    return len(ans)
}
```

Simplified version
```Python3 []
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        ans = []
        for num in nums:
            if len(ans) > 1 and ((ans[-2] > ans[-1] and num < ans[-1]) or (ans[-2] < ans[-1] and num > ans[-1])):
                ans[-1] = num
            elif not ans or ans[-1] != num:
                ans.append(num)
        return len(ans)
```
```Go []
func wiggleMaxLength(nums []int) int {
    ans := []int{}
    for _, num := range nums {
        if v := len(ans); v > 1 && ((ans[v - 2] > ans[v - 1] && num < ans[v - 1]) || (ans[v - 2] < ans[v - 1] && num > ans[v - 1])) {
            ans[v - 1] = num
        } else if v == 0 || ans[v - 1] != num {
            ans = append(ans, num)
        }
    }
    return len(ans)
}
```
