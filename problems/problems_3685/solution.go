package problem3685

import (
	"encoding/json"
	"log"
	"strings"
)

func subsequenceSumAfterCapping(nums []int, k int) []bool {
	n := len(nums)
	freq := make([]int, n+1)
	for _, num := range nums {
		freq[num]++
	}
	ans := make([]bool, n)
	dp := make([]bool, k+1)
	dp[0] = true
	used := 0
	for i := range n {
		num := i + 1
		for range freq[num] {
			for x := k; x >= num; x-- {
				dp[x] = dp[x] || dp[x-num]
			}
		}
		used += freq[num]
		for j := range min(k/num, n-used) + 1 {
			if dp[k-num*j] {
				ans[i] = true
				break
			}
		}
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

	return subsequenceSumAfterCapping(nums, k)
}
