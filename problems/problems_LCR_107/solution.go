package problemLCR_107

import (
	"encoding/json"
	"log"
	"strings"
)

func updateMatrix(mat [][]int) [][]int {
	m, n := len(mat), len(mat[0])
	ans := make([][]int, m)
	for i := range ans {
		ans[i] = make([]int, n)
		for j := range ans[i] {
			ans[i][j] = 0x3f3f3f3f
		}
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if mat[i][j] == 0 {
				ans[i][j] = 0
			}
			if i > 0 {
				ans[i][j] = min(ans[i][j], ans[i-1][j]+1)
			}
			if j > 0 {
				ans[i][j] = min(ans[i][j], ans[i][j-1]+1)
			}
		}
	}
	for i := m - 1; i >= 0; i-- {
		for j := n - 1; j >= 0; j-- {
			if i < m-1 {
				ans[i][j] = min(ans[i][j], ans[i+1][j]+1)
			}
			if j < n-1 {
				ans[i][j] = min(ans[i][j], ans[i][j+1]+1)
			}
		}
	}
	return ans
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var mat [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &mat); err != nil {
		log.Fatal(err)
	}

	return updateMatrix(mat)
}
