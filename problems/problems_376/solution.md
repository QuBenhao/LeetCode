# [Python/Go] 贪心动态规划 o(n)

> slug: pythongo-tan-xin-dong-tai-gui-hua-on-by-mbqmm
> date: 2022-02-24
> tags: Go, Python, Python3
> question: Wiggle Subsequence (wiggle-subsequence)
> url: https://leetcode.cn/problems/wiggle-subsequence/solutions/FSOdMG/pythongo-tan-xin-dong-tai-gui-hua-on-by-mbqmm/

---
### 解题思路
维护一个最长摆动序列。

实际上就是贪心的选择所有下降序列的最小值、上升序列的最大值【比如一段上升序列中最多取两个值构成正摆动，那么取的值越大越方便下一次取出负摆动】。

这个做法的好处是可以如果题目要求，也可以直接将最长摆动序列返回

### 代码

```Python3 []
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        ans = []
        for num in nums:
            if len(ans) > 1:
                # 该正摆动了
                if ans[-2] > ans[-1]:
                    if num > ans[-1]:
                        ans.append(num)
                    else:
                        ans[-1] = num
                # 该负摆动了
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

简化写法
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