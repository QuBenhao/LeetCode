package problem1493

import (
	"encoding/json"
	"log"
	"strings"
)

func longestSubarray(nums []int) (ans int) {
	allOne := true
	for _, num := range nums {
		if num != 1 {
			allOne = false
			break
		}
	}
	n := len(nums)
	if allOne {
		return n - 1
	}
	last, cur := 0, 0
	for i := range n + 1 {
		if i == n || nums[i] != 1 {
			ans = max(ans, last+cur)
			last = cur
			cur = 0
		} else {
			cur++
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

	return longestSubarray(nums)
}
