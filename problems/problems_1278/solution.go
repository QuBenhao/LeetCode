package problem1278

import (
	"encoding/json"
	"log"
	"math"
	"strings"
)

func palindromePartition(s string, k int) int {
	n := len(s)
	minChange := make([][]int, n)
	for i := n - 1; i >= 0; i-- {
		minChange[i] = make([]int, n)
		for j := i + 1; j < n; j++ {
			minChange[i][j] = minChange[i+1][j-1]
			if s[i] != s[j] {
				minChange[i][j]++
			}
		}
	}
	// 简化为枚举右端点，最少需要改变的次数
	dp := minChange[0]
	for i := 1; i < k; i++ {
		// 左边至少要能割i-1次，所以右端点至少为i; 题目要求割k-1次，所有右端点在n-k+i的不会被用到
		// 共用同一个空间做dp时，因为依赖左边的值，所以需要倒序更新
		for r := n - k + i; r >= i; r-- {
			dp[r] = math.MaxInt / 2
			for l := i; l <= r; l++ {
				dp[r] = min(dp[r], dp[l-1]+minChange[l][r])
			}
		}
	}
	return dp[n-1]
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return palindromePartition(s, k)
}
