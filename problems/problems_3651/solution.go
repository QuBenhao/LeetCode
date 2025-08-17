package problem3651

import (
	"encoding/json"
	"log"
	"math"
	"strings"

	"github.com/emirpasic/gods/trees/redblacktree"
)

func minCost(grid [][]int, k int) int {
	m, n := len(grid), len(grid[0])
	dp := make([][][]int, k+1)
	for i := range dp {
		dp[i] = make([][]int, m)
		for j := range dp[i] {
			dp[i][j] = make([]int, n)
			for l := range dp[i][j] {
				dp[i][j][l] = math.MaxInt32
			}
		}
	}
	mp := redblacktree.NewWithIntComparator()
	dp[0][0][0] = 0
	for i := range m {
		for j := range n {
			if v, exist := mp.Get(-grid[i][j]); exist {
				points := v.([][2]int)
				points = append(points, [2]int{i, j})
				mp.Put(-grid[i][j], points)
			} else {
				mp.Put(-grid[i][j], [][2]int{{i, j}})
			}
			if i+1 < m {
				dp[0][i+1][j] = min(dp[0][i+1][j], dp[0][i][j]+grid[i+1][j])
			}
			if j+1 < n {
				dp[0][i][j+1] = min(dp[0][i][j+1], dp[0][i][j]+grid[i][j+1])
			}
		}
	}
	for kk := 1; kk <= k; kk++ {
		mn := math.MaxInt32
		for _, v := range mp.Values() {
			for _, point := range v.([][2]int) {
				mn = min(mn, dp[kk-1][point[0]][point[1]])
			}
			for _, point := range v.([][2]int) {
				dp[kk][point[0]][point[1]] = mn
			}
		}
		for i := range m {
			for j := range n {
				if i+1 < m {
					dp[kk][i+1][j] = min(dp[kk][i+1][j], dp[kk][i][j]+grid[i+1][j])
				}
				if j+1 < n {
					dp[kk][i][j+1] = min(dp[kk][i][j+1], dp[kk][i][j]+grid[i][j+1])
				}
			}
		}
	}
	ans := math.MaxInt32
	for i := range k + 1 {
		ans = min(ans, dp[i][m-1][n-1])
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var grid [][]int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &grid); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return minCost(grid, k)
}
