package problem3152

import (
	"encoding/json"
	"log"
	"strings"
)

func isArraySpecial(nums []int, queries [][]int) []bool {
	n := len(nums)
	preSum := make([]int, n)
	for i := 0; i < n-1; i++ {
		preSum[i+1] = preSum[i]
		if nums[i]&1 != nums[i+1]&1 {
			preSum[i+1]++
		}
	}
	ans := make([]bool, 0, len(queries))
	for _, query := range queries {
		l, r := query[0], query[1]
		ans = append(ans, preSum[r]-preSum[l] == r-l)
	}
	return ans
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var queries [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &queries); err != nil {
		log.Fatal(err)
	}

	return isArraySpecial(nums, queries)
}
