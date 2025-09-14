package problem3686

import (
	"encoding/json"
	"log"
	"strings"
)

const MOD = int(1e9 + 7)

func countStableSubsequences(nums []int) int {
	var dp0, dp1, dp00, dp01, dp10, dp11 int
	for _, num := range nums {
		if (num & 1) == 0 {
			dp0, dp00, dp10 = (dp0+1)%MOD, (dp00+dp0+dp10)%MOD, (dp10+dp1+dp01+dp11)%MOD
		} else {
			dp1, dp01, dp11 = (dp1+1)%MOD, (dp01+dp0+dp00+dp10)%MOD, (dp11+dp1+dp01)%MOD
		}
	}
	return (dp0 + dp1 + dp00 + dp01 + dp10 + dp11) % MOD
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return countStableSubsequences(nums)
}
