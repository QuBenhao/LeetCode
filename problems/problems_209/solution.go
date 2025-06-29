package problem209

import (
	"encoding/json"
	"log"
	"math"
	"strings"
)

func minSubArrayLen(target int, nums []int) int {
	left, prefixSum, ans := 0, 0, math.MaxInt32
	for right, num := range nums {
		prefixSum += num
		for prefixSum >= target {
			ans = min(ans, right-left+1)
			prefixSum -= nums[left]
			left++
		}
	}
	if ans == math.MaxInt32 {
		return 0
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var target int
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &target); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &nums); err != nil {
		log.Fatal(err)
	}

	return minSubArrayLen(target, nums)
}
