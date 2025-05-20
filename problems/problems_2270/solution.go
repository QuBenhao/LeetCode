package problem2270

import (
	"encoding/json"
	"log"
	"strings"
)

func waysToSplitArray(nums []int) (ans int) {
	n := len(nums)
	s := 0
	for _, num := range nums {
		s += num
	}
	leftSum := 0
	for i := range n - 1 {
		leftSum += nums[i]
		if leftSum >= s-leftSum {
			ans++
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return waysToSplitArray(nums)
}
