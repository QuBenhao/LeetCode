# [Python/Java/JavaScript/Go] 中位数

> slug: pythonjavajavascriptgo-zhong-wei-shu-din-wgz6
> date: 2022-05-18
> tags: Go, Java, JavaScript, Python, Python3
> question: Minimum Moves to Equal Array Elements II (minimum-moves-to-equal-array-elements-ii)
> url: https://leetcode.cn/problems/minimum-moves-to-equal-array-elements-ii/solutions/CWknZc/pythonjavajavascriptgo-zhong-wei-shu-din-wgz6/

---
### 解题思路
数轴上有n个点，求一个点使他们到这个点距离和的最小。
中位数有这样的性质: 所有数与中位数的绝对差之和最小。

这里不多赘述这个证明,只给出简单证明思路,感兴趣的可以自行百度。
假设有有序数列$a_1, a_2, \ldots , a_n$, 且$a_1 \le a_2 \le \ldots \le a_n$:
这个数$x$显然不该在$a_1$左边或者$a_n$右边，这样距离明显比在里面大。
当$a_1 \le x \le a_n$，不管怎么变化，最终结果都是$\lvert a_1 - x \rvert + \lvert a_n - x \rvert = a_n - a_1$。
【其实就是$\lvert a_1 - x \rvert + \lvert a_n - x \rvert \ge a_n - a_1$】
同样继续讨论$a_2 \le x \le a_n-1$和其他点。
会得到不等式 $\sum_{i=1}^n \lvert a_i - x \rvert \ge a_n - a_1 + a_{n-2} - a_2 + \ldots$

最后就会得到中位数性质。

### 代码

```Python3 []
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        return sum(abs(mid - num) for num in nums) if (mid := sorted(nums)[len(nums) // 2]) != inf else inf
```
```Java []
class Solution {
    public int minMoves2(int[] nums) {
        Arrays.sort(nums);
        int ans = 0, n = nums.length;
        for(int i = 0; i < n / 2; i++) {
            ans += nums[n - 1 - i] - nums[i];
        }
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {number[]} nums
 * @return {number}
 */
var minMoves2 = function(nums) {
    nums.sort((a, b) => a - b)
    let ans = 0
    for(let left = 0, right = nums.length - 1; left < right; left++) {
        ans += nums[right--] - nums[left]
    }
    return ans
};
```
```Go []
func minMoves2(nums []int) (ans int) {
    sort.Ints(nums)
    for left, n := 0, len(nums); left < n / 2; left++ {
        ans += nums[n - 1 - left] - nums[left]
    }
    return
}
```