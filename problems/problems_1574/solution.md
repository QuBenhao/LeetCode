# [Py/Java/Ts/Go/C] Two pointers

> slug: pyjavatsgoc-shuang-zhi-zhen-by-himymben-yrsa
> date: 2023-03-25
> tags: C, Go, Java, Python3, TypeScript
> question: Shortest Subarray to be Removed to Make Array Sorted (shortest-subarray-to-be-removed-to-make-array-sorted)
> url: https://leetcode.cn/problems/shortest-subarray-to-be-removed-to-make-array-sorted/solutions/BrATBJ/pyjavatsgoc-shuang-zhi-zhen-by-himymben-yrsa/

---
> Problem: [1574. 删除最短的子数组使剩余数组有序](https://leetcode.cn/problems/shortest-subarray-to-be-removed-to-make-array-sorted/description/)

[TOC]

# Intuition
> The removed subarray must be contiguous, so enumerate its two endpoints. The remaining prefix and suffix must both be nondecreasing. As the left endpoint moves right, the right endpoint cannot move left: if removing [i,j] makes arr[:i] + arr[j+1:] nondecreasing, then arr[i-1] <= arr[j+1]; a later left endpoint i' satisfies arr[i - 1] <= arr[i' - 1]. This allows a two-pointer approach.

# Approach
> For each left endpoint, use two pointers to find the corresponding right endpoint and minimize the removed length. Stop when the prefix decreases, since that point must be removed and the left endpoint cannot move farther right.

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
        # Find the longest nondecreasing suffix
        while j and arr[j] >= arr[j - 1]:
            j -= 1
        # Return immediately if the whole array is nondecreasing
        if not j:
            return 0
        i, ans = 0, j
        while i < len(arr) - 1:
            # Find the leftmost valid right endpoint for the current left endpoint
            while j < len(arr) and arr[j] < arr[i]:
                j += 1
            ans = min(ans, j - i - 1)
            # The prefix decreases; no later position can be the left endpoint
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
