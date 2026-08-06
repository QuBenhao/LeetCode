# [C/Py/Java/Ts/Go] 模拟

> slug: cpyjavatsgo-mo-ni-by-himymben-oj6u
> date: 2023-03-26
> tags: C, Go, Java, Python3, TypeScript
> question: Find Subarrays With Equal Sum (find-subarrays-with-equal-sum)
> url: https://leetcode.cn/problems/find-subarrays-with-equal-sum/solutions/CCj8Kd/cpyjavatsgo-mo-ni-by-himymben-oj6u/

---
> Problem: [2395. 和相等的子数组](https://leetcode.cn/problems/find-subarrays-with-equal-sum/description/)

[TOC]

# 思路
> 二维遍历或一维遍历+哈希表

# Code
```C []
bool findSubarrays(int* nums, int numsSize){
    for (int i = 0; i < numsSize - 2; i++) {
        for (int j = i + 1; j < numsSize - 1; j++) {
            if (nums[i] + nums[i + 1] == nums[j] + nums[j + 1]) {
                return true;
            }
        }
    }
    return false;
}
```
```Python3 []
class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        s = set()
        for a, b in pairwise(nums):
            if (c := a + b) in s:
                return True
            else:
                s.add(c)
        return False
```
```Java []
class Solution {
    public boolean findSubarrays(int[] nums) {
        Set<Integer> s = new HashSet<>();
        for (int i = 0; i < nums.length - 1; i++) {
            int c = nums[i] + nums[i + 1];
            if (s.contains(c)) {
                return true;
            } else {
                s.add(c);
            }
        }
        return false;
    }
}
```
```TypeScript []
function findSubarrays(nums: number[]): boolean {
    const s: Set<number> = new Set<number>()
    for (let i = 0; i < nums.length - 1; i++) {
        const c = nums[i] + nums[i + 1]
        if (s.has(c)) {
            return true
        } else {
            s.add(c)
        }
    }
    return false
};
```
```Go []
func findSubarrays(nums []int) bool {
    s := map[int]bool{}
    for i, num := range nums {
        if i < len(nums) - 1 {
            if c := num + nums[i + 1]; s[c] {
                return true
            } else {
                s[c] = true
            }
        }
    }
    return false
}
```
