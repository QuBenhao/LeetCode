package problem312

import (
	"encoding/json"
	"log"
	"strings"
)

func maxCoins(nums []int) int {
	n := len(nums)
	arr := make([]int, n+2)
	for i := 1; i <= n; i++ {
		arr[i] = nums[i-1]
	}
	arr[0] = 1
	arr[n+1] = 1
	dp := make([][]int, n+2)
	for i := 0; i < n+2; i++ {
		dp[i] = make([]int, n+2)
	}
	for length := 3; length <= n+2; length++ {
		for l := 0; l+length-1 < n+2; l++ {
			r := l + length - 1
			for k := l + 1; k < r; k++ {
				dp[l][r] = max(dp[l][r], dp[l][k]+dp[k][r]+arr[l]*arr[k]*arr[r])
			}
		}
	}
	return dp[0][n+1]
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(values[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return maxCoins(nums)
}
