package problemLCR_040

import (
	"encoding/json"
	"log"
	"strings"
)

func maximalRectangle(matrix []string) (ans int) {
	m := len(matrix)
	if m == 0 {
		return 0
	}
	n := len(matrix[0])
	height := make([]int, n+1)
	height[n] = -1
	for _, s := range matrix {
		var stack []int
		for j := range n + 1 {
			if j < n {
				if s[j] == '1' {
					height[j]++
				} else {
					height[j] = 0
				}
			}
			for len(stack) > 0 && height[j] < height[stack[len(stack)-1]] {
				k := stack[len(stack)-1]
				stack = stack[:len(stack)-1]
				var left int
				if len(stack) == 0 {
					left = -1
				} else {
					left = stack[len(stack)-1]
				}
				ans = max(ans, height[k]*(j-left-1))
			}
			stack = append(stack, j)
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var matrix []string

	if err := json.Unmarshal([]byte(inputValues[0]), &matrix); err != nil {
		log.Fatal(err)
	}

	return maximalRectangle(matrix)
}
