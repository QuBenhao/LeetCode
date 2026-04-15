# [Python/Java/TypeScript/Go] 模拟

> Author: Benhao
> Date: 2022-08-29
> Upvotes: 26
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
按题意排列即可

### 代码

```Python3 []
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums[::2], nums[1::2] = nums[:n], nums[n:]
        return nums
```
```Java []
class Solution {
    public int[] shuffle(int[] nums, int n) {
        int[] ans = new int[2 * n];
        for (int i = 0; i < n; i++) {
            ans[2 * i] = nums[i];
            ans[2 * i + 1] = nums[i + n];
        }
        return ans;
    }
}
```
```TypeScript []
function shuffle(nums: number[], n: number): number[] {
    const ans: number[] = new Array<number>(2 * n)
    for (let i = 0; i < n; i++) {
        ans[2 * i] = nums[i]
        ans[2 * i + 1] = nums[i + n]
    }
    return ans
};
```
```Go []
func shuffle(nums []int, n int) []int {
    ans := make([]int, 2 * n)
    for i := 0; i < n; i++ {
        ans[2 * i] = nums[i]
        ans[2 * i + 1] = nums[i + n]
    }
    return ans
}
```