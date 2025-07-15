package problem3201

import (
	"encoding/json"
	"log"
	"strings"
)

func maximumLength(nums []int) (ans int) {
	dp := make([]int, 4)
	for _, num := range nums {
		cur := num & 1
		for i := range 4 {
			if (i>>(dp[i]&1))&1 == cur {
				dp[i]++
				ans = max(ans, dp[i])
			}
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

	return maximumLength(nums)
}
