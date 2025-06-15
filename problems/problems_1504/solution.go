package problem1504

import (
	"encoding/json"
	"log"
	"strings"
)

func numSubmat(mat [][]int) (ans int) {
	n := len(mat[0])
	heights := make([]int, n)
	for _, row := range mat {
		var st []int
		prev := make([]int, n)
		preSum := 0
		for j, v := range row {
			if v == 0 {
				heights[j] = 0
			} else {
				heights[j]++
			}
			for len(st) > 0 && heights[st[len(st)-1]] >= heights[j] {
				preSum -= prev[st[len(st)-1]]
				st = st[:len(st)-1]
			}
			if len(st) == 0 {
				prev[j] = heights[j] * (j + 1)
			} else {
				prev[j] = heights[j] * (j - st[len(st)-1])
			}
			preSum += prev[j]
			st = append(st, j)
			ans += preSum
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var mat [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &mat); err != nil {
		log.Fatal(err)
	}

	return numSubmat(mat)
}
