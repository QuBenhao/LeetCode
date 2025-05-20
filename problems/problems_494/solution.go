package problem494

import (
	"encoding/json"
	"log"
	"strings"
)

func findTargetSumWays(nums []int, target int) int {
	// 正数和为a, 负数和为(s - a), a - (s - a) = target, a = (target + s) / 2
	t := target
	for _, num := range nums {
		target += num
	}
	if target%2 != 0 || target < 0 || target < 2*t {
		return 0
	}
	target >>= 1
	dp := make([]int, target+1)
	dp[0] = 1
	for _, num := range nums {
		for i := target; i >= num; i-- {
			dp[i] += dp[i-num]
		}
	}
	return dp[target]
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var nums []int
	var target int

	if err := json.Unmarshal([]byte(values[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &target); err != nil {
		log.Fatal(err)
	}

	return findTargetSumWays(nums, target)
}
