package problem3350

import (
	"encoding/json"
	"log"
	"strings"
)

func maxIncreasingSubarrays(nums []int) (ans int) {
	n := len(nums)
	last, cur := 0, 1
	for i := range n {
		if i == n-1 || nums[i+1] <= nums[i] {
			ans = max(ans, min(last, cur), cur/2)
			last = cur
			cur = 1
			continue
		}
		cur++
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return maxIncreasingSubarrays(nums)
}
