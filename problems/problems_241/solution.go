package problem241

import (
	"encoding/json"
	"log"
	"strconv"
	"strings"
)

func diffWaysToCompute(expression string) []int {
	n := len(expression)
	dp := make([][][]int, n)
	for i := range dp {
		dp[i] = make([][]int, n)
	}
	var dfs func(int, int) []int
	dfs = func(l, r int) []int {
		if dp[l][r] != nil {
			return dp[l][r]
		}
		if r < l {
			dp[l][r] = append(dp[l][r], 0)
			return dp[l][r]
		}
		if val, err := strconv.Atoi(expression[l : r+1]); err == nil {
			dp[l][r] = append(dp[l][r], val)
			return dp[l][r]
		}
		for i := l; i <= r; i++ {
			if expression[i] < '0' || expression[i] > '9' {
				leftVals := dfs(l, i-1)
				rightVals := dfs(i+1, r)
				for _, leftVal := range leftVals {
					for _, rightVal := range rightVals {
						var result int
						switch expression[i] {
						case '+':
							result = leftVal + rightVal
						case '-':
							result = leftVal - rightVal
						case '*':
							result = leftVal * rightVal
						}
						dp[l][r] = append(dp[l][r], result)
					}
				}
			}
		}
		return dp[l][r]
	}

	return dfs(0, n-1)
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var expression string

	if err := json.Unmarshal([]byte(inputValues[0]), &expression); err != nil {
		log.Fatal(err)
	}

	return diffWaysToCompute(expression)
}
