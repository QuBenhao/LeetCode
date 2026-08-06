# [Python/Java/JavaScript] 数学 

> slug: pythonjavajavascript-shu-xue-by-himymben-j1wh
> date: 2021-10-19
> tags: Java, JavaScript, Python, Python3
> question: Minimum Moves to Equal Array Elements (minimum-moves-to-equal-array-elements)
> url: https://leetcode.cn/problems/minimum-moves-to-equal-array-elements/solutions/qpQ9Jo/pythonjavajavascript-shu-xue-by-himymben-j1wh/

---
### 解题思路
每次能让n-1个数加1，相当于每次能让一个数减1。既然是一个数减一，那么相等必然需要都等于最小的那个数，统计每个数到最小的数的距离。

### 代码

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