# [Python/Java/JavaScript/Go] Median

> slug: pythonjavajavascriptgo-zhong-wei-shu-din-wgz6
> date: 2022-05-18
> tags: Go, Java, JavaScript, Python, Python3
> question: Minimum Moves to Equal Array Elements II (minimum-moves-to-equal-array-elements-ii)
> url: https://leetcode.cn/problems/minimum-moves-to-equal-array-elements-ii/solutions/CWknZc/pythonjavajavascriptgo-zhong-wei-shu-din-wgz6/

---
### Approach
Given n points on a number line, find a point minimizing the sum of distances to them.
The median minimizes the sum of absolute differences from all values.

I will only outline the proof; search for more detail if interested.
Let $a_1, a_2, \ldots , a_n$ be sorted so that $a_1 \le a_2 \le \ldots \le a_n$:
The value $x$ should not lie to the left of $a_1$ or to the right of $a_n$, since that clearly gives a greater distance sum than a point inside.
For $a_1 \le x \le a_n$, changing x leaves $\lvert a_1 - x \rvert + \lvert a_n - x \rvert = a_n - a_1$ unchanged.
[More generally, $\lvert a_1 - x \rvert + \lvert a_n - x \rvert \ge a_n - a_1$.]
Apply the same reasoning to $a_2 \le x \le a_n-1$ and the remaining points.
This gives $\sum_{i=1}^n \lvert a_i - x \rvert \ge a_n - a_1 + a_{n-2} - a_2 + \ldots$.

The median property follows.

### Code

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
