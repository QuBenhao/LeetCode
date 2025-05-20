package problem908

import (
	"encoding/json"
	"log"
	"strings"
)

func smallestRangeI(nums []int, k int) int {
	minVal, maxVal := nums[0], nums[0]
	for _, num := range nums {
		if num < minVal {
			minVal = num
		}
		if num > maxVal {
			maxVal = num
		}
	}

	if maxVal-minVal <= 2*k {
		return 0
	}
	return maxVal - minVal - 2*k
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return smallestRangeI(nums, k)
}
