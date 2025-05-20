package problem2845

import (
	"encoding/json"
	"log"
	"strings"
)

func countInterestingSubarrays(nums []int, modulo int, k int) (ans int64) {
	n := len(nums)
	preSum := make([]int, n+1)
	for i := 1; i <= n; i++ {
		preSum[i] = preSum[i-1]
		if nums[i-1]%modulo == k {
			preSum[i]++
		}
	}
	counter := make(map[int]int)
	counter[0] = 1
	for i := 1; i <= n; i++ {
		target := (preSum[i] - k + modulo) % modulo
		ans += int64(counter[target])
		counter[preSum[i]%modulo]++
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var modulo int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &modulo); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &k); err != nil {
		log.Fatal(err)
	}

	return countInterestingSubarrays(nums, modulo, k)
}
