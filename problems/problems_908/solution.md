# [Python/Java/JavaScript/Go] 数学

> Author: Benhao
> Date: 2022-04-29
> Upvotes: 23
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
为了得到最低分数,我们需要减小数组中最大值和最小值的差异。
我们希望最大值尽可能小,最小值尽可能大,来减小差异 (注意最终最大值是大于等于最终最小值的)。

如果最大值$nums_i$和最小值$nums_j$可以变为共同的某个数,那么所有数都可以变成这个数,最终答案为0。 ($nums_i - k \le nums_j + k$)
如果最大值的最小值($nums_i-k$)都比最小值的最大值($nums_j+k$)大的话, 那么最终答案(最低分数)是$nums_i-nums_j-2*k$。 ($nums_i - k \gt nums_j + k$)

### 代码

```Python3 []
class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        return max(0, max(nums) - min(nums) - 2 * k)
```
```Java []
class Solution {
    public int smallestRangeI(int[] nums, int k) {
        int max = 0, min = 10001;
        for(int num: nums) {
            max = Math.max(num, max);
            min = Math.min(num, min);
        }
        return Math.max(0, max - min - 2 * k);
    }
}
```
```JavaScript []
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var smallestRangeI = function(nums, k) {
    let max = 0, min = 10001
    for(const num of nums) {
        max = Math.max(num, max)
        min = Math.min(num, min)
    }
    return Math.max(0, max - min - 2 * k)
};
```
```Go []
func smallestRangeI(nums []int, k int) int {
    max, min := 0, 10001
    for _, num := range nums {
        if num > max {
            max = num
        }
        if num < min {
            min = num
        }
    }
    if v := max - min - 2 * k; v >= 0 {
        return v
    }
    return 0
}
```