package problem862

import (
	"encoding/json"
	"log"
	"strings"
)

func shortestSubarray(nums []int, k int) int {
	dq := [][2]int{{0, -1}} // (sum, index)
	ans := len(nums) + 1
	prefixSum := 0
	for i, num := range nums {
		prefixSum += num
		for len(dq) > 0 && prefixSum-dq[0][0] >= k {
			ans = min(ans, i-dq[0][1])
			dq = dq[1:] // pop from front
		}
		for len(dq) > 0 && prefixSum <= dq[len(dq)-1][0] {
			dq = dq[:len(dq)-1] // pop from back
		}
		dq = append(dq, [2]int{prefixSum, i})
	}
	if ans == len(nums)+1 {
		return -1
	}
	return ans
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

	return shortestSubarray(nums, k)
}
