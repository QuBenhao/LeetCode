package problemLCR_039

import (
	"encoding/json"
	"log"
	"strings"
)

func largestRectangleArea(heights []int) (ans int) {
	heights = append(heights, -1)
	var stack []int
	for i, h := range heights {
		for len(stack) > 0 && h < heights[stack[len(stack)-1]] {
			j := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			var left int
			if len(stack) == 0 {
				left = -1
			} else {
				left = stack[len(stack)-1]
			}
			ans = max(ans, heights[j]*(i-left-1))
		}
		stack = append(stack, i)
	}
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var heights []int

	if err := json.Unmarshal([]byte(inputValues[0]), &heights); err != nil {
		log.Fatal(err)
	}

	return largestRectangleArea(heights)
}
