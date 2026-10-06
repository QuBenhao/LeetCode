# [Python/Go/C++/Java] Sorting and a greedy approach

> Author: Benhao
> Date: 2024-04-09
> Upvotes: 2
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [452. 用最少数量的箭引爆气球](https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/description/)

[TOC]

# Intuition

> Sort by right endpoint in ascending order and shoot as far right as possible. If the current shot falls within an interval, no additional shot is needed for it.

# Approach

> Greedily count the minimum required arrows

# Complexity

Time complexity:
> $O(n * log_n)$

Space complexity:
> $O(1)$



# Code
```Python3 []
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        cur, ans = points[0][1], 1
        for a, b in points:
            if a > cur:
                ans += 1
                cur = b
        return ans
```
```Golang []
func findMinArrowShots(points [][]int) int {
	sort.Slice(points, func(i, j int) bool {
		return points[i][1] < points[j][1]
	})
	cur, ans := points[0][1], 1
	for _, point := range points {
		if point[0] > cur {
			ans++
			cur = point[1]
		}
	}
	return ans
}
```
```Java []
class Solution {
    public int findMinArrowShots(int[][] points) {
        Arrays.sort(points, Comparator.comparingInt(a -> a[1]));
        int cur = points[0][1], ans = 1;
        for (int[] point: points) {
            if (point[0] > cur) {
                ans++;
                cur = point[1];
            }
        }
        return ans;
    }
}
```
```C++ []
class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        std::ranges::sort(points, [](const vector<int>& a, const vector<int>& b) {
            return a[1] < b[1];
        });
        int cur = points[0][1], ans = 1;
        for (auto point: points) {
            if (point[0] > cur) {
                ans++;
                cur = point[1];
            }
        }
        return ans;
    }
};
```
  
