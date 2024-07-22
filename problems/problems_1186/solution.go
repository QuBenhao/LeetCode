package problem1186

import (
	"encoding/json"
	"log"
	"math"
	"strings"
)

func maximumSum(arr []int) int {
	ans, dp0, dp1 := math.MinInt32, math.MinInt32, math.MinInt32
	for _, v := range arr {
		dp1 = max(dp0, dp1+v)
		dp0 = max(dp0+v, v)
		ans = max(ans, max(dp0, dp1))
	}
	return ans
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var arr []int

	if err := json.Unmarshal([]byte(inputValues[0]), &arr); err != nil {
		log.Fatal(err)
	}

	return maximumSum(arr)
}
