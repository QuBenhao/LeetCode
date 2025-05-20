package problem698

import (
	"encoding/json"
	"log"
	"strings"
)

func canPartitionKSubsets(nums []int, k int) bool {
	n := len(nums)
	sum := 0
	for _, num := range nums {
		sum += num
	}
	if sum%k != 0 {
		return false
	}
	target := sum / k
	for _, num := range nums {
		if num > target {
			return false
		}
	}
	allPicked := 1<<n - 1
	dp := make([]int, 1<<n)
	for i := 1; i < 1<<n; i++ {
		dp[i] = -1
	}
	for i := 0; i <= allPicked; i++ {
		for j := 0; j < n; j++ {
			if (i>>j)&1 != 0 {
				before := i & ^(1 << j)
				if dp[before] != -1 && dp[before]+nums[j] <= target {
					dp[i] = (dp[before] + nums[j]) % target
				}
			}
		}
	}
	return dp[allPicked] == 0
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

	return canPartitionKSubsets(nums, k)
}
