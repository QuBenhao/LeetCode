package problem3349

import (
	"encoding/json"
	"log"
	"strings"
)

func hasIncreasingSubarrays(nums []int, k int) bool {
	a, b := 0, k
	n := len(nums) - k
out:
	for b <= n {
		for j := a + 1; j < b; j++ {
			if nums[j] <= nums[j-1] {
				b += j - a
				a += j - a
				continue out
			}
		}
		for j := b + 1; j < b+k; j++ {
			if nums[j] <= nums[j-1] {
				a += j - b
				b += j - b
				continue out
			}
		}
		return true
	}
	return false
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

	return hasIncreasingSubarrays(nums, k)
}
