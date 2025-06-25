package problem1802

import (
	"encoding/json"
	"log"
	"strings"
)

func maxValue(n int, index int, maxSum int) int {
	helper := func(mid int) bool {
		var left, right int
		if mid > index {
			left = (mid - 1 + mid - index) * index / 2
		} else {
			left = (mid-1+1)*(mid-1)/2 + (index - mid + 1)
		}
		if mid > n-index-1 {
			right = (mid - 1 + mid - (n - index - 1)) * (n - index - 1) / 2
		} else {
			right = (mid-1+1)*(mid-1)/2 + (n - index - 1 - mid + 1)
		}
		return left+right <= maxSum-mid
	}
	left, right := 1, maxSum-n+1
	for left < right {
		mid := (left + right + 1) / 2
		if helper(mid) {
			left = mid
		} else {
			right = mid - 1
		}
	}
	return left
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var index int
	var maxSum int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &index); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &maxSum); err != nil {
		log.Fatal(err)
	}

	return maxValue(n, index, maxSum)
}
