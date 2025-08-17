package problem3653

import (
	"encoding/json"
	"log"
	"strings"
)

const mod = 1_000_000_007

func xorAfterQueries(nums []int, queries [][]int) int {
	for _, query := range queries {
		l, r, k, v := query[0], query[1], query[2], query[3]
		for i := l; i <= r; i += k {
			nums[i] = int((int64(nums[i]) * int64(v)) % mod)
		}
	}
	ans := 0
	for _, num := range nums {
		ans ^= num
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var queries [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &queries); err != nil {
		log.Fatal(err)
	}

	return xorAfterQueries(nums, queries)
}
