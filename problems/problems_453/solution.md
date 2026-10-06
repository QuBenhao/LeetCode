# [Python/Java/JavaScript] Mathematics 

> slug: pythonjavajavascript-shu-xue-by-himymben-j1wh
> date: 2021-10-19
> tags: Java, JavaScript, Python, Python3
> question: Minimum Moves to Equal Array Elements (minimum-moves-to-equal-array-elements)
> url: https://leetcode.cn/problems/minimum-moves-to-equal-array-elements/solutions/qpQ9Jo/pythonjavajavascript-shu-xue-by-himymben-j1wh/

---
### Approach
Incrementing n-1 values by 1 is equivalent to decrementing one value by 1. With decrements, all values must reach the minimum, so sum each value's distance from that minimum.

### Code

```Python3 []
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - min(nums) * len(nums)
```
```Java []
class Solution {
    public int minMoves(int[] nums) {
        int min = Integer.MAX_VALUE;
        for(int num: nums)
            min = Math.min(num, min);
        int ans = 0;
        for(int num: nums)
            ans += num - min;
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {number[]} nums
 * @return {number}
 */
var minMoves = function(nums) {
    const min = Math.min(...nums);
    let ans = 0;
    for(const num of nums)
        ans += num - min;
    return ans;
};
```
