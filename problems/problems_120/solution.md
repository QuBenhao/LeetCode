# [Python/Go/C++/Java] Dynamic programming

> Author: Benhao
> Date: 2024-03-05
> Upvotes: 3
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [120. 三角形最小路径和](https://leetcode.cn/problems/triangle/description/)

[TOC]

# Intuition

> Rolling updates

# Approach

> The minimum path sum at row i, column j is formed by adding the current value to the smaller of the sums at row i-1, column j-1 and row i-1, column j. The leftmost column is accumulated directly.

# Complexity

Time complexity:
> $O(n)$

Space complexity:
> $O(n)$ [$O(1)$ when reusing the original array]



# Code
```Python3 []
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [inf] * n
        dp[0] = 0
        for i, tr in enumerate(triangle):
            for j in range(i, 0, -1):
                dp[j] = min(dp[j - 1], dp[j]) + tr[j]
            dp[0] += tr[0]
        return min(dp)
```
```C++ []
class Solution {
public:
  int minimumTotal(const vector<vector<int>> &triangle) {
    int n = triangle.size();
    vector<int> dp(n);
    for (int i = 0; i < n; ++i) {
      if (i > 0) {
        dp[i] = dp[i - 1] + triangle[i][i];
      }
      for (int j = i - 1; j > 0; --j) {
        dp[j] = min(dp[j], dp[j - 1]) + triangle[i][j];
      }
      dp[0] += triangle[i][0];
    }
    return *min_element(dp.begin(), dp.end());
  }
};
```
```Go []
func minimumTotal(triangle [][]int) int {
	n := len(triangle)
	for i := 1; i < n; i++ {
		for j := 1; j < i; j++ {
			triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])
		}
		triangle[i][i] += triangle[i-1][i-1]
		triangle[i][0] += triangle[i-1][0]
	}
	ans := triangle[n-1][0]
	for i := 1; i < n; i++ {
		ans = min(ans, triangle[n-1][i])
	}
	return ans
}
```
```Java []
class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int n = triangle.size();
        int[] dp = new int[n];
        dp[0] = triangle.get(0).get(0);
        for (int i = 1; i < n; ++i) {
            var cur = triangle.get(i);
            dp[i] = cur.getLast() + dp[i - 1];
            for (int j = i - 1; j > 0; --j) {
                dp[j] = Math.min(dp[j - 1], dp[j]) + cur.get(j);
            }
            dp[0] += cur.getFirst();
        }
        int ans = dp[0];
        for (int i = 1; i < n; ++i) {
            ans = Math.min(ans, dp[i]);
        }
        return ans;
    }
}
```

Reuse the original array directly
```Python3 []
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        for i in range(1, n):
            for j in range(1, i):
                triangle[i][j] = min(triangle[i - 1][j], triangle[i - 1][j - 1]) + triangle[i][j]
            triangle[i][0] += triangle[i - 1][0]
            triangle[i][i] += triangle[i - 1][i - 1]
        return min(triangle[n - 1])
```
