# [Python/Java/TypeScript/Go] 异或

> slug: pythonjavatypescriptgo-by-himymben-4qfg
> date: 2022-09-26
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Missing Two LCCI (missing-two-lcci)
> url: https://leetcode.cn/problems/missing-two-lcci/solutions/sXhPS9/pythonjavatypescriptgo-by-himymben-4qfg/

---
### 解题思路
首先得到两个缺失的数的异或值，找到他们任意一个不同的二进制位(这里采用lowbit)。
按这个二进制位区分原来的异或和，我们将得到其中一个数。

### 代码

```Python3 []
class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        n, xor = len(nums) + 2, 0
        for num in nums:
            xor ^= num
        for num in range(1, n + 1):
            xor ^= num
        i = xor&-xor
        cur = 0
        for num in range(1, n + 1):
            if i & num:
                cur ^= num
        for num in nums:
            if i & num:
                cur ^= num
        return [cur, xor ^ cur]
```
```Java []
class Solution {
    public int[] missingTwo(int[] nums) {
        int xor = 0, n = nums.length + 2;
        for (int num: nums) {
            xor ^= num;
        }
        for (int i = 1; i <= n; i++) {
            xor ^= i;
        }
        int lowbit = xor & -xor, cur = 0;
        for (int num: nums) {
            if ((num & lowbit) > 0) {
                cur ^= num;
            }
        }
        for (int i = 1; i <= n; i++) {
            if ((i & lowbit) > 0) {
                cur ^= i;
            }
        }
        return new int[]{cur, xor ^ cur};
    }
}
```
```TypeScript []
function missingTwo(nums: number[]): number[] {
    const n: number = nums.length + 2
    let xor: number = 0
    for (const num of nums) {
        xor ^= num
    }
    for (let i = 1; i <= n; i++) {
        xor ^= i
    }
    const lowbit: number = xor & -xor
    let cur: number = 0
    for (const num of nums) {
        if ((num & lowbit) > 0) {
            cur ^= num
        }
    }
    for (let i = 1; i <= n; i++) {
        if ((i & lowbit) > 0) {
            cur ^= i
        }
    }
    return [cur, xor ^ cur]
};
```
```Go []
func missingTwo(nums []int) []int {
    n, xor := len(nums) + 2, 0
    for _, num := range nums {
        xor ^= num
    }
    for i := 1; i <= n; i++ {
        xor ^= i
    }
    cur, lowbit := 0, xor & -xor
    for _, num := range nums {
        if num & lowbit > 0 {
            cur ^= num
        }
    }
    for i := 1; i <= n; i++ {
        if i & lowbit > 0 {
            cur ^= i
        }
    }
    return []int{cur, xor ^ cur}
}
```