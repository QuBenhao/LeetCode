package problem3495

import (
	"encoding/json"
	"log"
	"math/bits"
	"strings"
)

func minOperations(queries [][]int) (ans int64) {
	helper := func(s, m int64) int64 {
		if m > s-m {
			return m
		}
		return (s + 1) / 2
	}
	var preSum func(num uint32) int64
	preSum = func(num uint32) int64 {
		if num == 0 {
			return 0
		}
		b := (33 - bits.LeadingZeros32(num)) / 2
		last := uint32(1) << (2*b - 2)
		return preSum(last-1) + int64(b)*int64(num+1-last)
	}
	for _, query := range queries {
		mx := (33 - bits.LeadingZeros32(uint32(query[1]))) / 2
		sm := preSum(uint32(query[1])) - preSum(uint32(query[0]-1))
		ans += helper(sm, int64(mx))
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var queries [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &queries); err != nil {
		log.Fatal(err)
	}

	return minOperations(queries)
}
