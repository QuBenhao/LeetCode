package problem84

import (
	"encoding/json"
	"log"
	"strings"
)

func largestRectangleArea(heights []int) (ans int) {
	var stack []int
	heights = append([]int{0}, heights...)
	heights = append(heights, 0)
	for i, h := range heights {
		for len(stack) > 0 && h < heights[stack[len(stack)-1]] {
			height := heights[stack[len(stack)-1]]
			stack = stack[:len(stack)-1]
			ans = max(ans, height*(i-stack[len(stack)-1]-1))
		}
		stack = append(stack, i)
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var heights []int

	if err := json.Unmarshal([]byte(inputValues[0]), &heights); err != nil {
		log.Fatal(err)
	}

	return largestRectangleArea(heights)
}
