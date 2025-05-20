package problem1673

import (
	"encoding/json"
	"log"
	"strings"
)

func mostCompetitive(nums []int, k int) []int {
	ans := make([]int, k)
	for i, m, n := 0, 0, len(nums); i < n; i++ {
		for m > 0 && nums[i] < ans[m-1] && m+n-i > k {
			m--
		}
		if m < k {
			ans[m] = nums[i]
			m++
		}
	}
	return ans
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var nums []int
	var k int

	if err := json.Unmarshal([]byte(values[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &k); err != nil {
		log.Fatal(err)
	}

	return mostCompetitive(nums, k)
}
