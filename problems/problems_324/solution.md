# [Python/Java/TypeScript/Go] 排序贪心

> slug: pythonjavatypescriptgo-by-himymben-q6nj
> date: 2022-06-27
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Wiggle Sort II (wiggle-sort-ii)
> url: https://leetcode.cn/problems/wiggle-sort-ii/solutions/6eGQC1/pythonjavatypescriptgo-by-himymben-q6nj/

---
### 解题思路
写在前面，本解法不满足进阶的条件。
题目给定了所有输入数组都可以得到满足题目要求的结果，
按题目条件我们想偶数坐标位填小一些的数，奇数坐标位填大一些的数，想到排序后分成两部分。
但是这两部分的分界处可能是一样大的，比如[4,5,5,6]的分界在5。
为了保证一样大的数会被错开，我们可以将前部分倒序填入，同时为了保证一定比它大，后部分也要倒序填入。

### 代码

```Python3 []
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        nums[::2], nums[1::2] = nums[:(len(nums) + 1) // 2][::-1], nums[(len(nums) + 1)//2:][::-1]
```
```Java []
class Solution {
    public void wiggleSort(int[] nums) {
        int[] cp = Arrays.copyOf(nums, nums.length);
        Arrays.sort(cp);
        for(int idx = 0, i = (nums.length + 1 >> 1) - 1, j = nums.length - 1; idx < nums.length; i--, j--, idx++) {
            nums[idx++] = cp[i];
            if(idx < nums.length) {
                nums[idx] = cp[j];
            }
        }
    }
}
```
```TypeScript []
/**
 Do not return anything, modify nums in-place instead.
 */
function wiggleSort(nums: number[]): void {
    const [...cp] = nums, n = nums.length
    cp.sort((a, b) => a - b)
    for (let i = Math.floor((n + 1) / 2) - 1, j = n - 1, idx = 0; idx < n; idx++, i--, j--) {
        nums[idx++] = cp[i]
        if (idx < n) {
            nums[idx] = cp[j]
        }
    }
};
```
```Go []
func wiggleSort(nums []int)  {
    n := len(nums)
    cp := append([]int{}, nums...)
    sort.Ints(cp)
    for idx, i, j := 0, (n + 1) / 2 - 1, n - 1; idx < n; {
        nums[idx] = cp[i]
        idx++
        if idx < n {
            nums[idx] = cp[j]
            j--
            idx++
        }
        i--
    }
}
```