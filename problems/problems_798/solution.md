# [Python/Java/JavaScript/Go] Difference array

> slug: pythonjavajavascriptgo-chai-fen-shu-zu-b-xhvy
> date: 2022-03-08
> tags: Go, Java, JavaScript, Python, Python3
> question: Smallest Rotation with Highest Score (smallest-rotation-with-highest-score)
> url: https://leetcode.cn/problems/smallest-rotation-with-highest-score/solutions/VnNi6u/pythonjavajavascriptgo-chai-fen-shu-zu-b-xhvy/

---
### Approach
The problem statement gives the following brute-force implementation
```python3
class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        diff = [num - i for i, num in enumerate(nums)]
        # num - i ===> num - (i - k) % len(nums)
        ans, mx = 0, sum(d <= 0 for d in diff)
        for k in range(1, len(nums)):
            if (s := sum(num - (i - k) % len(nums) <= 0 for i, num in enumerate(nums))) > mx:
                ans, mx = k, s
        return ans
```

Both index i and value num affect whether rotation k makes the value minus its index at this position at most 0. As k changes continuously, this difference changes continuously too.
Can we determine in advance which range of k makes the difference between i and num satisfy the condition, without knowing k itself?

For a value num, its value minus its final index is at most 0 only when the index is in `[num, n-1]`; the difference is clearly positive for indices in `[0, num-1]`.
We can use this range and the value of i to determine which rotations k satisfy the condition.

Consider the cases:
If i initially lies in `[num, n-1]`, it contributes to the answer without any rotation: `diff[0]+=1`;
As k increases, i moves left past num and stops contributing: `diff[i - num + 1] -= 1`;
Continuing past the leftmost position `0` wraps it to `n-1`, where it contributes again: `diff[i + 1] += 1`.

If i initially lies in `[0, num - 1]`, it contributes nothing without rotation. Moving past the leftmost position `0` and wrapping to `n-1` makes it contribute: `diff[i + 1] += 1`;
Continuing past `num` into `[0, num - 1]` makes it stop contributing again: `diff[i - num + n + 1] -= 1`.

Scan diff while tracking how many indices have a difference at most 0 at each step, then return the smallest k that achieves the largest count.


### Code

```Python3 []
class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        diff = [0] * (n + 1)
        # num ---> n - 1
        for i, num in enumerate(nums):
            if i >= num:
                diff[0] += 1
                diff[i - num + 1] -= 1
                diff[i + 1] += 1
            else:
                diff[i + 1] += 1
                diff[i - num + n + 1] -= 1
        ans = cur = mx = 0
        for i in range(n):
            cur += diff[i]
            if cur > mx:
                ans, mx = i, cur
        return ans
```
```Java []
class Solution {
    public int bestRotation(int[] nums) {
        int n = nums.length;
        int[] diff = new int[n + 1];
        for(int i = 0; i < n; i++) {
            if(i >= nums[i]) {
                diff[0]++;
                diff[i - nums[i] + 1]--;
                diff[i + 1]++;
            } else {
                diff[i + 1]++;
                diff[i - nums[i] + n + 1]--;
            }
        }
        int ans = 0, cur = 0, max = 0;
        for(int i = 0; i < n; i++) {
            cur += diff[i];
            if(cur > max) {
                ans = i;
                max = cur;
            }
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
var bestRotation = function(nums) {
    const n = nums.length
    const diff = new Array(n + 1).fill(0)
    for(let i = 0; i < n; i++) {
        if(i >= nums[i]) {
            diff[0]++
            diff[i - nums[i] + 1]--
            diff[i + 1]++
        } else {
            diff[i + 1]++
            diff[i - nums[i] + n + 1]--
        }
    }
    let ans = 0, cur = 0, max = 0
    for(let i = 0; i < n; i++) {
        cur += diff[i]
        if(cur > max) {
            ans = i
            max = cur
        } 
    }
    return ans
};
```
```Go []
func bestRotation(nums []int) (ans int) {
    n := len(nums)
    diff := make([]int, n + 1)
    for i := 0; i < n; i++ {
        if num := nums[i]; i >= num {
            diff[0]++
            diff[i - num + 1]--
            diff[i + 1]++
        } else {
            diff[i + 1]++
            diff[i - num + n + 1]--
        }
    }
    for i, cur, max := 0, 0, 0; i < n; i++ {
        cur += diff[i]
        if cur > max {
            ans, max = i, cur
        }
    }
    return
}
```
