# [Py/Java/Ts/Go/C] 双指针

> slug: pyjavatsgoc-shuang-zhi-zhen-by-himymben-yrsa
> date: 2023-03-25
> tags: C, Go, Java, Python3, TypeScript
> question: Shortest Subarray to be Removed to Make Array Sorted (shortest-subarray-to-be-removed-to-make-array-sorted)
> url: https://leetcode.cn/problems/shortest-subarray-to-be-removed-to-make-array-sorted/solutions/BrATBJ/pyjavatsgoc-shuang-zhi-zhen-by-himymben-yrsa/

---
> Problem: [1574. 删除最短的子数组使剩余数组有序](https://leetcode.cn/problems/shortest-subarray-to-be-removed-to-make-array-sorted/description/)

[TOC]

# 思路
> 题目要求删除的是子数组，而不是子序列，子数组是连续的，我们可以采用枚举这个数组的两端。因为最终整体是单调的，也就是左端点的左边和右端点的右边是单调的。那么当左边端点往右移动时，右边端点不可能往左移动（假设左端点i，右端点j的时候，arr[:i] + arr[j+1:]满足单调，那么arr[i-1] <= arr[j+1]，而左端点右移后新的左端点i'满足arr[i - 1] <= arr[i' - 1]），所以可以使用双指针。

# 解题方法
> 双指针，枚举左端点对应的右端点，看最小的是哪个。注意当左端点出现拐点时，说明这里必须删除，没有必要继续右移了。

# Code
```C []
#define MIN(a, b) (((a) < (b)) ? (a) : (b))
int findLengthOfShortestSubarray(int* arr, int arrSize){
    int j;
    for (j = arrSize - 1; j > 0 && arr[j - 1] <= arr[j]; j--) {}
    if (j == 0) {
        return 0;
    }
    int i = 0, ans = j;
    do {
        while (j < arrSize && arr[j] < arr[i] && ++j) {}
        ans = MIN(ans, j - i - 1);
    }
    while (i < arrSize - 1 && arr[i + 1] >= arr[i] && ++i);
    return ans;
}
```
```Python3 []

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        j = len(arr) - 1
        # 统计右端点最长单调区间
        while j and arr[j] >= arr[j - 1]:
            j -= 1
        # 整体单调直接返回
        if not j:
            return 0
        i, ans = 0, j
        while i < len(arr) - 1:
            # 枚举当前左端点的最左右端点
            while j < len(arr) and arr[j] < arr[i]:
                j += 1
            ans = min(ans, j - i - 1)
            # 左端点出现拐点，后面的点不可能作为左端点
            if arr[i + 1] < arr[i]:
                break
            i += 1
        return ans
```
```Java []
class Solution {
    public int findLengthOfShortestSubarray(int[] arr) {
        int n = arr.length, j;
        for (j = n - 1; j > 0 && arr[j] >= arr[j - 1]; j--) {}
        if (j == 0) {
            return 0;
        }
        int i = 0, ans = j;
        do {
            while (j < n && arr[j] < arr[i] && ++j > 0) {}
            ans = Math.min(ans, j - i - 1);
        } while (i < n - 1 && arr[i + 1] >= arr[i] && ++i > 0);
        return ans;
    }
}
```
```TypeScript []
function findLengthOfShortestSubarray(arr: number[]): number {
    let n: number = arr.length, j: number
    for (j = n - 1; j > 0 && arr[j - 1] <= arr[j]; j--) {}
    if (j == 0) {
        return 0
    }
    let i: number = 0, ans: number = j
    do {
        while (j < n && arr[j] < arr[i] && ++j) {}
        ans = Math.min(ans, j - i - 1)
    } while (i < n - 1 && arr[i + 1] >= arr[i] && ++i > 0)
    return ans
};
```
```Go []
func findLengthOfShortestSubarray(arr []int) (ans int) {
    j := len(arr) - 1
    for ; j > 0 && arr[j] >= arr[j - 1]; j-- {}
    if j == 0 {
        return
    }
    ans = j
    for i := 0; i < len(arr) - 1; i++ {
        for ; j < len(arr) && arr[j] < arr[i]; j++ {}
        ans = min(ans, j - i - 1)
        if arr[i + 1] < arr[i] {
            return
        }
    }
    return
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
```
