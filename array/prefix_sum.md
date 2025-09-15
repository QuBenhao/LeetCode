# 前缀和

$`prefix\_sum[i] = \sum_{k=0}^{i-1} nums[k]`$

$`prefix\_sum[i] - prefix\_sum[j] = \sum_{k=j}^{i-1} nums[k]`$

```python
from itertools import accumulate


def pivot_index(nums) -> int:
    pre_sum = [0] + list(accumulate(nums))
    for i, num in enumerate(nums):
        if pre_sum[i] == pre_sum[-1] - pre_sum[i + 1]:
            return i
    return -1
```

```go
package main

func pivotIndex(nums []int) int {
	n := len(nums)
	prefixSum := make([]int, n+1)
	for i := 0; i < n; i++ {
		prefixSum[i+1] = prefixSum[i] + nums[i]
	}
	for i := 0; i < n; i++ {
		if prefixSum[i] == prefixSum[n]-prefixSum[i+1] {
			return i
		}
	}
	return -1
}
```

## 二维前缀和

$`prefix\_sum[i][j] = \sum_{k=0}^{i-1} \sum_{l=0}^{j-1} matrix[k][l]`$

$
`prefix\_sum[i][j] - prefix\_sum[i][l] - prefix\_sum[k][j] + prefix\_sum[k][l] = \sum_{x=k}^{i-1} \sum_{y=l}^{j-1} matrix[x][y]`$

```python
def sum_region(matrix, row1, col1, row2, col2):
    m = len(matrix)
    if m == 0:
        return 0
    n = len(matrix[0])
    pre_sum = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            pre_sum[i][j] = pre_sum[i - 1][j] + pre_sum[i][j - 1] - pre_sum[i - 1][j - 1] + matrix[i - 1][j - 1]
    return pre_sum[row2 + 1][col2 + 1] - pre_sum[row1][col2 + 1] - pre_sum[row2 + 1][col1] + pre_sum[row1][col1]
```

```go
package main

type NumMatrix struct {
    preSum [][]int
}

func Constructor(matrix [][]int) NumMatrix {
    m := len(matrix)
    if m == 0 {
        return NumMatrix{}
    }
    n := len(matrix[0])
    preSum := make([][]int, m+1)
    for i := range preSum {
        preSum[i] = make([]int, n+1)
    }
    
    for i := 1; i <= m; i++ {
        for j := 1; j <= n; j++ {
            preSum[i][j] = preSum[i-1][j] + preSum[i][j-1] - preSum[i-1][j-1] + matrix[i-1][j-1]
        }
    }
    return NumMatrix{preSum: preSum}
}

func (this *NumMatrix) SumRegion(row1 int, col1 int, row2 int, col2 int) int {
    return this.preSum[row2+1][col2+1] - this.preSum[row1][col2+1] - this.preSum[row2+1][col1] + this.preSum[row1][col1]
}
```