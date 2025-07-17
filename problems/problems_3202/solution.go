package problem3202

import (
	"encoding/json"
	"log"
	"strings"
)

func maximumLength(nums []int, k int) (ans int) {
	for val := range k {
		dp := make([]int, k)
		for _, num := range nums {
			num %= k
			dp[num] = dp[(k+val-num)%k] + 1
			ans = max(ans, dp[num])
		}
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

	return maximumLength(nums, k)
}
