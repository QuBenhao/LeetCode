# [Python/Go/C++/Java/Ts/Rust] 排序

> Author: Benhao
> Date: 2024-03-07
> Upvotes: 2
> Tags: C, C++, Go, Java, Python3, Rust, TypeScript

---


> Problem: [56. 合并区间](https://leetcode.cn/problems/merge-intervals/description/)

[TOC]

# 思路

> 排序后可以保证左端点是递增的，然后依次判断相邻的有无交集即可

# 解题方法

> 如果有交集，就扩充当前区间的终点

# 复杂度

时间复杂度:
> $O(nlog_n)$

空间复杂度:
> $O(n)$



# Code
```Python3 []
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()
        slow = fast = 0
        while fast < len(intervals):
            cur = intervals[slow][1]
            while fast < len(intervals) and intervals[fast][0] <= cur:
                cur = max(cur, intervals[fast][1])
                fast += 1
            ans.append([intervals[slow][0], cur])
            slow = fast
        return ans
```
```Golang []
func merge(intervals [][]int) (ans [][]int) {
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})
	for _, interval := range intervals {
		left, right := interval[0], interval[1]
		if len(ans) == 0 || ans[len(ans)-1][1] < left {
			ans = append(ans, interval)
		} else {
			ans[len(ans)-1][1] = max(ans[len(ans)-1][1], right)
		}
	}
	return
}
```
```C++ []
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> ans;
        sort(intervals.begin(), intervals.end());
        for (auto interval: intervals) {
            if (ans.empty() || ans.back()[1] < interval[0]) {
                ans.emplace_back(interval);
            } else {
                ans.back()[1] = max(ans.back()[1], interval[1]);
            }
        }
        return ans;
    }
};
```
```Java []
public class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, Comparator.comparingInt(a -> a[0]));
        List<int[]> ans = new ArrayList<>();
        for (int[] interval: intervals) {
            if (ans.isEmpty() || ans.getLast()[1] < interval[0]) {
                ans.add(interval);
            } else {
                ans.getLast()[1] = Math.max(ans.getLast()[1], interval[1]);
            }
        }
        return ans.toArray(new int[ans.size()][]);
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] intervals = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(merge(intervals));
    }
}
```
```typescript []
function merge(intervals: number[][]): number[][] {
	intervals.sort((a, b) => a[0] - b[0]);
	const merged: number[][] = [];
	for (const interval of intervals) {
		if (merged.length === 0 || merged[merged.length - 1][1] < interval[0]) {
			merged.push(interval);
		} else {
			merged[merged.length - 1][1] = Math.max(merged[merged.length - 1][1], interval[1]);
		}
	}
	return merged;
};
```
```rust []
impl Solution {
    pub fn merge(intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
		let mut intervals = intervals;
		intervals.sort_unstable_by(|a, b| a[0].cmp(&b[0]));
		let mut merged: Vec<Vec<i32>> = Vec::new();
		for interval in intervals {
			if let Some(last) = merged.last_mut() {
				if interval[0] <= last[1] {
					last[1] = last[1].max(interval[1]);
				} else {
					merged.push(interval);
				}
			} else {
				merged.push(interval);
			}
		}
		merged
    }
}
```
  
