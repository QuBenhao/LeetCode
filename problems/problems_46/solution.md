# [Python] Permutations

> Author: Benhao
> Date: 2024-03-11
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [46. 全排列](https://leetcode.cn/problems/permutations/description/)

[TOC]

# Intuition

> Enumerate which number to place at each position until all positions are filled.

# Approach

> Put the chosen number in position and swap the original number to the back for a later choice.


# Code
```Python3 []
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans, n = [], len(nums)

        def dfs(x):
            if x == n - 1:
                ans.append(list(nums))
                return
            for i in range(x, n):
                nums[x], nums[i] = nums[i], nums[x]
                dfs(x + 1)
                nums[x], nums[i] = nums[i], nums[x]
        
        dfs(0)
        return ans
```
```C []
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
#define MAX_LEN (6 * 5 * 4 * 3 * 2 + 1)


void swap(int *nums, int i, int j) {
    int tmp = nums[i];
    nums[i] = nums[j];
    nums[j] = tmp;
}

void dfs(int *nums, int numsSize, int**ans,  int *ansIdx, int **returnColumnSizes, int x) {
    if (x == numsSize - 1) {
        ans[*ansIdx] = (int *) malloc(sizeof(int) * numsSize);
        memcpy(ans[*ansIdx], nums, sizeof(int) * numsSize);
        (*returnColumnSizes)[*ansIdx] = numsSize;
        (*ansIdx)++;
    }

    for (int i = x; i < numsSize; i++) {
        swap(nums, x, i);
        dfs(nums, numsSize, ans, ansIdx, returnColumnSizes, x + 1);
        swap(nums, x, i);
    }
}


int** permute(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    int **ans = (int **) malloc(sizeof(int *) * MAX_LEN);
    *returnColumnSizes = (int *) malloc(sizeof(int) * MAX_LEN);
    *returnSize = 0;
    dfs(nums, numsSize, ans, returnSize, returnColumnSizes, 0);
    return ans;
}
```
```Java []
class Solution {

    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }

    private void dfs(int[] nums, List<List<Integer>> ans, int x) {
        if (x == nums.length - 1) {
            ans.add(Arrays.stream(nums).boxed().toList());
            return;
        }
        for (int i = x; i < nums.length; i++) {
            swap(nums, x, i);
            dfs(nums, ans, x + 1);
            swap(nums, x, i);
        }
    }

    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        dfs(nums, ans, 0);
        return ans;
    }
}
```
  
