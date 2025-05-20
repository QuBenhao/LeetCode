package problem2302

import (
	"encoding/json"
	"log"
	"strings"
)

func countSubarrays(nums []int, k int64) (ans int64) {
	left, cur := 0, int64(0)
	for right, num := range nums {
		cur += int64(num)
		for cur*int64(right-left+1) >= k {
			cur -= int64(nums[left])
			left++
		}
		ans += int64(right - left + 1)
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var k int64

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return countSubarrays(nums, k)
}
