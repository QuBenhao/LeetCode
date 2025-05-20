package problem3537

import (
	"encoding/json"
	"log"
	"strings"
)

func specialGrid(N int) [][]int {
	n := 1 << N
	ans := make([][]int, n)
	for i := 0; i < n; i++ {
		ans[i] = make([]int, n)
	}

	var dfs func(int, int, int, int) int
	dfs = func(start int, left int, row int, length int) int {
		if length == 1 {
			ans[row][left] = start
			return start + 1
		}
		halfLength := length >> 1
		leftHalf := left + halfLength
		rowHalf := row + halfLength
		nxt := dfs(start, leftHalf, row, halfLength)
		nxt = dfs(nxt, leftHalf, rowHalf, halfLength)
		nxt = dfs(nxt, left, rowHalf, halfLength)
		return dfs(nxt, left, row, halfLength)
	}
	dfs(0, 0, 0, n)
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var N int

	if err := json.Unmarshal([]byte(inputValues[0]), &N); err != nil {
		log.Fatal(err)
	}

	return specialGrid(N)
}
