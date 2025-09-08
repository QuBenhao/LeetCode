package problem2327

import (
	"encoding/json"
	"log"
	"strings"
)

const MOD int = 1e9 + 7

func peopleAwareOfSecret(n int, delay int, forget int) int {
	preSum := make([]int, n+1)
	preSum[1] = 1
	for i := 2; i <= n; i++ {
		inc := (preSum[max(i-delay, 0)] - preSum[max(i-forget, 0)]) % MOD
		preSum[i] = (preSum[i-1] + inc) % MOD
	}
	return ((preSum[n]-preSum[max(n-forget, 0)])%MOD + MOD) % MOD
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var delay int
	var forget int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &delay); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &forget); err != nil {
		log.Fatal(err)
	}

	return peopleAwareOfSecret(n, delay, forget)
}
