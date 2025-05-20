package problemLCR_009

import (
	"encoding/json"
	"log"
	"strings"
)

func numSubarrayProductLessThanK(nums []int, k int) (ans int) {
	for cur, left, right := 1, 0, 0; right < len(nums); right++ {
		cur *= nums[right]
		for cur >= k && left <= right {
			cur /= nums[left]
			left++
		}
		ans += right - left + 1
	}
	return
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

	return numSubarrayProductLessThanK(nums, k)
}
