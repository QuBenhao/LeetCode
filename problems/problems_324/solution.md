# [Python/Java/TypeScript/Go] Sorting and a greedy approach

> slug: pythonjavatypescriptgo-by-himymben-q6nj
> date: 2022-06-27
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Wiggle Sort II (wiggle-sort-ii)
> url: https://leetcode.cn/problems/wiggle-sort-ii/solutions/6eGQC1/pythonjavatypescriptgo-by-himymben-q6nj/

---
### Approach
First, this solution does not meet the follow-up requirements.
The problem guarantees that every input array has a valid arrangement.
We want smaller values at even indices and larger values at odd indices, suggesting sorting and splitting the array into two parts.
However, the values at the boundary may be equal, as with the two 5s in [4,5,5,6].
To separate equal values, insert the first part in reverse order. Insert the second part in reverse order as well to ensure its paired values are larger.

### Code

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
