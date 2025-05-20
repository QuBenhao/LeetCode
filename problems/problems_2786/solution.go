package problem2786

import (
	"encoding/json"
	"log"
	"math"
	"strings"
)

func maxScore(nums []int, x int) int64 {
	ans := int64(nums[0])
	dp := []int64{math.MinInt32, math.MinInt32}
	dp[nums[0]%2] = int64(nums[0])
	for i := 1; i < len(nums); i++ {
		idx := nums[i] % 2
		cur := max(dp[idx]+int64(nums[i]), dp[idx^1]+int64(nums[i])-int64(x))
		ans = max(ans, cur)
		dp[idx] = max(dp[idx], cur)
	}
	return ans
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var nums []int
	var x int

	if err := json.Unmarshal([]byte(values[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &x); err != nil {
		log.Fatal(err)
	}

	return maxScore(nums, x)
}
