# [Python/Java/JavaScript/Go] 排序 + 二分

> Author: Benhao
> Date: 2022-05-19
> Upvotes: 18
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
既然每个区间的start是唯一的,那么我们按start排序(保留原坐标),
然后对每个区间二分找它的右侧区间即可。

### 代码 

```Python3 []
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        return [lt[idx][1] if (idx := bisect_left(lt, b, key=lambda x:x[0])) < len(lt) else -1 for _, b in intervals] if (lt := sorted([[inter[0], i] for i, inter in enumerate(intervals)])) else []
```
```Java []
class Solution {
    public int[] findRightInterval(int[][] intervals) {
        int n = intervals.length;
        int[][] startIdxs = new int[n][2];
        for(int i = 0; i < n; i++) {
            startIdxs[i][0] = intervals[i][0];
            startIdxs[i][1] = i;
        }
        Arrays.sort(startIdxs, (a, b) -> a[0] - b[0]);
        int[] ans = new int[n];
        Arrays.fill(ans, -1);
        for(int i = 0; i < n; i++) {
            int left = 0, right = n;
            while(left < right) {
                int mid = left + right >> 1;
                if(startIdxs[mid][0] < intervals[i][1]) {
                    left = mid + 1;
                } else {
                    right = mid;
                }
            }
            if(left < n) {
                ans[i] = startIdxs[left][1];
            }
        }
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {number[][]} intervals
 * @return {number[]}
 */
var findRightInterval = function(intervals) {
    const n = intervals.length
    const startIdxs = new Array(n).fill(0).map(() => new Array(2).fill(0))
    for(let i = 0; i < n; i++) {
        startIdxs[i][0] = intervals[i][0]
        startIdxs[i][1] = i
    }
    startIdxs.sort((a, b) => a[0] - b[0])
    const ans = new Array(n).fill(-1)
    for(let i = 0; i < n; i++) {
        let left = 0, right = n
        while(left < right) {
            const mid = left + right >> 1
            if(startIdxs[mid][0] < intervals[i][1]) {
                left = mid + 1
            } else {
                right = mid
            }
        }
        if(left < n) {
            ans[i] = startIdxs[left][1]
        }
    }
    return ans
};
```
```Go []
func findRightInterval(intervals [][]int) []int {
    n := len(intervals)
    startIdxs := make([][]int, n)
    for i, interval := range intervals {
        startIdxs[i] = []int{interval[0], i}
    }
    sort.Slice(startIdxs, func(i, j int) bool {
        return startIdxs[i][0] < startIdxs[j][0]
    })
    ans := make([]int, n)
    for i := 0; i < n; i++ {
        left, right := 0, n
        for left < right {
            mid := (left + right) >> 1
            if startIdxs[mid][0] < intervals[i][1] {
                left = mid + 1
            } else {
                right = mid
            }
        }
        if left < n {
            ans[i] = startIdxs[left][1]
        } else {
            ans[i] = -1
        }
    }
    return ans
}
```