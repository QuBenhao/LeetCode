package problem2210

import (
	"encoding/json"
	"log"
	"strings"
)

func diffToSign(diff int) int {
	if diff > 0 {
		return 1
	} else if diff < 0 {
		return -1
	}
	return 0
}

func countHillValley(nums []int) (ans int) {
	n := len(nums)
	last, lastDiff := nums[0], 0
	for i := 0; i < n; i++ {
		for i < n-1 && nums[i] == nums[i+1] {
			i++
		}
		curDiff := diffToSign(nums[i] - last)
		if lastDiff*curDiff < 0 {
			ans++
		}
		last, lastDiff = nums[i], curDiff
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return countHillValley(nums)
}
