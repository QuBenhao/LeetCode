package problem2044

import (
	"encoding/json"
	"log"
	"math/bits"
	"strings"
)

func countMaxOrSubsets(nums []int) (ans int) {
	n := len(nums)
	maxOr := 0
	mask := 1 << n
	dp := make([]int, mask)
	for i := 1; i < mask; i++ {
		lowbit := i & -i
		prev := i ^ lowbit
		idx := 31 - bits.LeadingZeros32(uint32(lowbit)) // Get the index of the lowest bit set
		dp[i] = dp[prev] | nums[idx]
		if dp[i] > maxOr {
			maxOr = dp[i]
			ans = 1
		} else if dp[i] == maxOr {
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

	return countMaxOrSubsets(nums)
}
