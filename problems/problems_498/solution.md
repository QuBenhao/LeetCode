# [Python/Java/TypeScript/Go/C++] 不等式推导

> Author: Benhao
> Date: 2022-06-13
> Upvotes: 49
> Tags: C++, Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
首先要知道的是：
1. 右斜对角线是横纵坐标和为定值(左斜的话是差为定值)。
2. 一共有$m + n - 1$个对角线，对应左上角贴边走到右下角

根据以上条件，可以推导每个对角线的横纵坐标范围，再确认一下从上到下还是从下到上即可。
```python3
            # 已知 x + y = k 和 0 <= x < m 还有 0 <= y < n
            # 0 <= x < m, 0 <= k - x < n
            # 0 <= x < m, k - n < x <= k
```

### 代码

```Python3 []
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n, ans = len(mat), len(mat[0]), []
        for k in range(m + n - 1):
            if not k % 2:
                ans += [mat[x][k-x] for x in range(min(m - 1, k), max(-1, k - n),-1)]
            else:
                ans += [mat[x][k-x] for x in range(max(0, k - n + 1), min(k + 1, m))]
        return ans
```
```Java []
class Solution {
    public int[] findDiagonalOrder(int[][] mat) {
        int m = mat.length, n = mat[0].length;
        int[] ans = new int[m * n];
        for(int k = 0, idx = 0; k < m + n - 1; k++) {
            if ((k & 1) == 1) {
                for(int x = Math.max(0, k - n + 1); x < Math.min(k + 1, m); x++) {
                    ans[idx++] = mat[x][k - x];
                }
            } else {
                for (int x = Math.min(k, m - 1); x >= Math.max(0, k - n + 1); x--) {
                    ans[idx++] = mat[x][k - x];
                }
            }
        }
        return ans;
    }
}
```
```TypeScript []
function findDiagonalOrder(mat: number[][]): number[] {
    const m = mat.length, n = mat[0].length, ans = new Array()
        for(let k = 0; k < m + n - 1; k++) {
            if ((k & 1) == 1) {
                for(let x = Math.max(0, k - n + 1); x < Math.min(k + 1, m); x++) {
                    ans.push(mat[x][k - x])
                }
            } else {
                for (let x = Math.min(k, m - 1); x >= Math.max(0, k - n + 1); x--) {
                    ans.push(mat[x][k - x])
                }
            }
        }
        return ans
};
```
```Go []
func findDiagonalOrder(mat [][]int) (ans []int) {
    for m, n, k := len(mat), len(mat[0]), 0; k < m + n - 1; k++ {
        if k & 1 == 1 {
            for x := max(0, k - n + 1); x < min(k + 1, m); x++ {
                ans = append(ans, mat[x][k - x])
            }
        } else {
            for x := min(k, m - 1); x >= max(0, k - n + 1); x-- {
                ans = append(ans, mat[x][k - x])
            }
        }
    }
    return
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
```
```C++ []
class Solution {
public:
  vector<int> findDiagonalOrder(const vector<vector<int>> &mat) {
    int m = mat.size(), n = mat[0].size();
    vector<int> result(m * n);
    int idx = 0;
    for (int k = 0; k < m + n; ++k) {
      int x, d;
      int upper = min(k, m - 1), lower = max(0, k - n + 1);
      if (k % 2 == 0) {
        x = upper;
        d = -1;
      } else {
        x = lower;
        d = 1;
      }
      while (x >= lower && x <= upper) {
        result[idx++] = mat[x][k - x];
        x += d;
      }
    }
    return result;
  }
};
```