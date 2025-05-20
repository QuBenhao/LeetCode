package problemLCR_012

import (
	"encoding/json"
	"log"
	"strings"
)

func pivotIndex(nums []int) int {
	n := len(nums)
	prefixSum := make([]int, n+1)
	for i := 0; i < n; i++ {
		prefixSum[i+1] = prefixSum[i] + nums[i]
	}
	for i := 0; i < n; i++ {
		if prefixSum[i] == prefixSum[n]-prefixSum[i+1] {
			return i
		}
	}
	return -1
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return pivotIndex(nums)
}
