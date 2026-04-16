# [Python/C/Go/Java/Typescript] 二分查找/遍历

> Author: Benhao
> Date: 2024-03-15
> Upvotes: 2
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [57. 插入区间](https://leetcode.cn/problems/insert-interval/description/)

[TOC]

# 思路

> 1. 二分查找插入点，合并插入即可
> 2. 遍历比较区间大小，合并插入区间

# 解题方法

> 二分查找、模拟

# 复杂度

时间复杂度:
> 二分$O(log_n)$
> 遍历$O(n)$

空间复杂度:
> $O(n)$



# Code
```Python3 []
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l_idx = bisect_left(intervals, newInterval[0], key=lambda x: x[1])
        r_idx = bisect_right(intervals, newInterval[1], key=lambda x: x[0]) - 1
        return intervals[:l_idx] + [[min(intervals[l_idx][0], newInterval[0]), max(intervals[r_idx][1], newInterval[1])]] + intervals[r_idx + 1:] if l_idx < len(intervals) and r_idx >= 0 else (intervals + [newInterval] if l_idx == len(intervals) else [newInterval] + intervals)
```
```Python3 []
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans, left, right = [], newInterval[0], newInterval[1]
        for a, b in intervals:
            if b < left or a > right:
                if a > right:
                    ans.append([left, right])
                    left = right = inf
                ans.append([a, b])
            else:
                left = min(left, a)
                right = max(right, b)
        if left != inf and (not ans or ans[-1][1] < left):
            ans.append([left, right])
        return ans
```
```C []
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
#define MIN(a, b) (((a) < (b)) ? (a) : (b))
#define MAX(a, b) (((a) < (b)) ? (b) : (a))

int** insert(int** intervals, int intervalsSize, int* intervalsColSize, int* newInterval, int newIntervalSize, int* returnSize, int** returnColumnSizes) {
    bool add = false;
    int **ans = malloc(sizeof(int *) * (intervalsSize + 1));
    *returnColumnSizes = malloc(sizeof(int *) * (intervalsSize + 1));
    *returnSize = 0;
    int left = newInterval[0], right = newInterval[1];
    for (int i = 0; i < intervalsSize; i++) {
        int a = intervals[i][0], b = intervals[i][1];
        if (b < left || a > right) {
            if (!add && a > right) {
                ans[*returnSize] = malloc(sizeof(int) * 2);
                (*returnColumnSizes)[*returnSize] = 2;
                ans[*returnSize][0] = left;
                ans[(*returnSize)++][1] = right;
                add = true;
            }
            ans[*returnSize] = malloc(sizeof(int) * 2);
            (*returnColumnSizes)[*returnSize] = 2;
            ans[*returnSize][0] = a;
            ans[(*returnSize)++][1] = b;
        } else {
            left = MIN(left, a);
            right = MAX(right, b);
        }
    }
    if (!add) {
        ans[*returnSize] = malloc(sizeof(int) * 2);
        (*returnColumnSizes)[*returnSize] = 2;
        ans[*returnSize][0] = left;
        ans[(*returnSize)++][1] = right;
    }
    return ans; 
}
```
```Go []
func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func insert(intervals [][]int, newInterval []int) (ans [][]int) {
    left, right := newInterval[0], newInterval[1]
    for _, interval := range intervals {
        a, b := interval[0], interval[1]
        if b < left || a > right {
            if a > right {
                ans = append(ans, []int{left, right})
                left = 0x3f3f3f
                right = 0x3f3f3f
            }
            ans = append(ans, interval)
        } else {
            left = min(left, a)
            right = max(right, b)
        }
    }
    if left != 0x3f3f3f && (len(ans) == 0 || ans[len(ans) - 1][1] < left) {
        ans = append(ans, []int{left, right})
    }
    return
}
```
```Java []
class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> ans = new ArrayList<>();
        int left = newInterval[0], right = newInterval[1];
        for (int[] interval: intervals) {
            int a = interval[0], b = interval[1];
            if (b < left || a > right) {
                if (a > right) {
                    ans.add(new int[]{left, right});
                    left = right = 0x3f3f3f;
                }
                ans.add(new int[]{a, b});
            } else {
                left = Math.min(left, a);
                right = Math.max(right, b);
            }
        }
        if (left != 0x3f3f3f && (ans.size() == 0 || ans.get(ans.size() - 1)[1] < left)) {
            ans.add(new int[]{left, right});
        }
        return ans.toArray(new int[0][0]);
    }
}
```
```TypeScript []
function insert(intervals: number[][], newInterval: number[]): number[][] {
    let [left, right] = newInterval
    const ans: number[][] = []
    for (const [a, b] of intervals) {
        if (b < left || a > right) {
            if (a > right) {
                ans.push([left, right])
                left = right = 0x3f3f3f
            }
            ans.push([a, b])
        } else {
            left = Math.min(left, a)
            right = Math.max(right, b)
        }
    }
    if (left != 0x3f3f3f && (ans.length == 0 || ans[ans.length - 1][1] < left)) {
        ans.push([left, right])
    }
    return ans
};
```
  
