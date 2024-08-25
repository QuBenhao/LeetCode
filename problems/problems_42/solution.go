package problem42

import (
	"encoding/json"
	"log"
	"strings"
)

func trap(height []int) (ans int) {
	n := len(height)
	leftMax := make([]int, n)
	rightMax := make([]int, n)
	for i := 1; i < n; i++ {
		leftMax[i] = max(leftMax[i-1], height[i-1])
		rightMax[n-i-1] = max(rightMax[n-i], height[n-i])
	}
	for i, h := range height {
		if minHeight := min(leftMax[i], rightMax[i]); minHeight > h {
			ans += minHeight - h
		}
	}
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var height []int

	if err := json.Unmarshal([]byte(inputValues[0]), &height); err != nil {
		log.Fatal(err)
	}

	return trap(height)
}
