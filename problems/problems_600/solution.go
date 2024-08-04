package problem600

import (
	"encoding/json"
	"log"
	"strings"
)

func findIntegers(n int) (ans int) {
	// dp[i] 表示长度为 i 的二进制不包含连续的 1 的个数
	dp := make([]int, 31)
	dp[0], dp[1] = 1, 2
	for i := 2; i < 31; i++ {
		dp[i] = dp[i-1] + dp[i-2]
	}
	n++
	pre := 0
	for i := 29; i >= 0; i-- {
		if n&(1<<i) != 0 {
			ans += dp[i]
			if pre == 1 {
				return
			}
			pre = 1
		} else {
			pre = 0
		}
	}
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return findIntegers(n)
}
