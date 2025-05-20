package problem2965

import (
	"encoding/json"
	"log"
	"strings"
)

func findMissingAndRepeatedValues(grid [][]int) []int {
	n := len(grid)
	cnt := make([]int, n*n+1)
	for _, row := range grid {
		for _, x := range row {
			cnt[x]++
		}
	}

	ans := make([]int, 2)
	for i := 1; i <= n*n; i++ {
		if cnt[i] == 2 {
			ans[0] = i // 出现两次的数
		} else if cnt[i] == 0 {
			ans[1] = i // 出现零次的数
		}
	}
	return ans
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var grid [][]int

	if err := json.Unmarshal([]byte(values[0]), &grid); err != nil {
		log.Fatal(err)
	}

	return findMissingAndRepeatedValues(grid)
}
