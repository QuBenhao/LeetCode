package problem3578

import (
	"encoding/json"
	"log"
	"strings"
)

const MOD = 1000000007

func countPartitions(nums []int, k int) int {
	var minQueue []int
	var maxQueue []int
	n := len(nums)
	left := 0
	dp := make([]int, n+1)
	dp[0] = 1
	sumF := 0
	for i := range n {
		sumF = (sumF + dp[i]) % MOD
		for len(minQueue) > 0 && nums[minQueue[len(minQueue)-1]] >= nums[i] {
			minQueue = minQueue[:len(minQueue)-1]
		}
		minQueue = append(minQueue, i)
		for len(maxQueue) > 0 && nums[maxQueue[len(maxQueue)-1]] <= nums[i] {
			maxQueue = maxQueue[:len(maxQueue)-1]
		}
		maxQueue = append(maxQueue, i)
		for nums[maxQueue[0]]-nums[minQueue[0]] > k {
			sumF = (sumF - dp[left] + MOD) % MOD
			left++
			if minQueue[0] < left {
				minQueue = minQueue[1:]
			}
			if maxQueue[0] < left {
				maxQueue = maxQueue[1:]
			}
		}
		dp[i+1] = sumF
	}
	return dp[n]
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

	return countPartitions(nums, k)
}
