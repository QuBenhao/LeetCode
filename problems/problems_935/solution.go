package problem935

import (
	"encoding/json"
	"log"
	"strings"
)

const MOD = 1000_000_007

func modSum(values ...int) (ans int) {
	for _, v := range values {
		ans = (ans + v) % MOD
	}
	return
}

func arrModSum(values []int) (ans int) {
	for _, v := range values {
		ans = (ans + v) % MOD
	}
	return
}

func knightDialer(n int) int {
	if n == 1 {
		return 10
	}
	/*
		1: 6, 8
		2: 7, 9
		3: 4, 8
		4: 3, 9, 0
		5: -
		6: 1, 7, 0
		7: 2, 6
		8: 1, 3
		9: 2, 4
		0: 4, 6
	*/
	// dp = [[1] * 10 for _ in range(2)]
	dp := make([][]int, 2)
	for i := range dp {
		dp[i] = make([]int, 10)
		if i == 0 {
			for j := range dp[i] {
				if j == 5 {
					continue
				}
				dp[i][j] = 1
			}
		}
	}
	for i := range n {
		if i == 0 {
			continue
		}
		dp[i%2][0] = modSum(dp[(i-1)%2][4], dp[(i-1)%2][6])
		dp[i%2][1] = modSum(dp[(i-1)%2][6], dp[(i-1)%2][8])
		dp[i%2][2] = modSum(dp[(i-1)%2][7], dp[(i-1)%2][9])
		dp[i%2][3] = modSum(dp[(i-1)%2][4], dp[(i-1)%2][8])
		dp[i%2][4] = modSum(dp[(i-1)%2][3], dp[(i-1)%2][9], dp[(i-1)%2][0])
		dp[i%2][6] = modSum(dp[(i-1)%2][1], dp[(i-1)%2][7], dp[(i-1)%2][0])
		dp[i%2][7] = modSum(dp[(i-1)%2][2], dp[(i-1)%2][6])
		dp[i%2][8] = modSum(dp[(i-1)%2][1], dp[(i-1)%2][3])
		dp[i%2][9] = modSum(dp[(i-1)%2][2], dp[(i-1)%2][4])
	}
	return arrModSum(dp[(n-1)%2])
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return knightDialer(n)
}
