package problem2438

import (
	"encoding/json"
	"log"
	"math/bits"
	"strings"
)

const MOD = 1e9 + 7

var POWERS [436]int

func init() {
	POWERS[0] = 1
	for i := 1; i < 436; i++ {
		POWERS[i] = POWERS[i-1] * 2 % MOD
	}
}

func productQueries(n int, queries [][]int) []int {
	preSum := []int{0}
	for n > 0 {
		lowbit := n & -n
		length := 31 - bits.LeadingZeros32(uint32(lowbit))
		preSum = append(preSum, preSum[len(preSum)-1]+length)
		n ^= lowbit
	}
	ans := make([]int, 0, len(queries))
	for _, query := range queries {
		left, right := query[0], query[1]
		ans = append(ans, POWERS[preSum[right+1]-preSum[left]])
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var queries [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &queries); err != nil {
		log.Fatal(err)
	}

	return productQueries(n, queries)
}
