package problem3652

import (
	"encoding/json"
	"log"
	"strings"
)

func maxProfit(prices []int, strategy []int, k int) (ans int64) {
	n := len(prices)
	preSum, originPreSum := make([]int64, n+1), make([]int64, n+1)
	for i := range n {
		preSum[i+1] = preSum[i] + int64(prices[i])*int64(strategy[i])
		originPreSum[i+1] = originPreSum[i] + int64(prices[i])
	}
	ans = 0
	for i := range n - k + 1 {
		cur := preSum[i] - preSum[i+k]
		cur += originPreSum[i+k] - originPreSum[i+k/2]
		ans = max(ans, cur)
	}
	ans += preSum[n]
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var prices []int
	var strategy []int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &prices); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &strategy); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &k); err != nil {
		log.Fatal(err)
	}

	return maxProfit(prices, strategy, k)
}
