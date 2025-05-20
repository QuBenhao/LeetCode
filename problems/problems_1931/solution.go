package problem1931

import (
	"encoding/json"
	"log"
	"strings"
)

const mod = 1_000_000_007

func colorTheGrid(m int, n int) (ans int) {
	pow3 := make([]int, m)
	pow3[0] = 1
	for i := 1; i < m; i++ {
		pow3[i] = pow3[i-1] * 3
	}

	var valid []int
next:
	for color := range pow3[m-1] * 3 {
		for i := range m - 1 {
			if color/pow3[i+1]%3 == color/pow3[i]%3 { // 相邻颜色相同
				continue next
			}
		}
		valid = append(valid, color)
	}

	nv := len(valid)
	nxt := make([][]int, nv)
	for i, color1 := range valid {
	next2:
		for j, color2 := range valid {
			for _, p3 := range pow3 {
				if color1/p3%3 == color2/p3%3 { // 相邻颜色相同
					continue next2
				}
			}
			nxt[i] = append(nxt[i], j)
		}
	}

	dp := make([][]int, 2)
	for i := range dp {
		dp[i] = make([]int, nv)
	}
	for j := range valid {
		dp[0][j] = 1
	}
	for i := 1; i < n; i++ {
		for j := range valid {
			dp[i%2][j] = 0
			for _, k := range nxt[j] {
				dp[i%2][j] = (dp[i%2][j] + dp[(i-1)%2][k]) % mod
			}
		}
	}
	for _, v := range dp[(n-1)%2] {
		ans = (ans + v) % mod
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var m int
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &m); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &n); err != nil {
		log.Fatal(err)
	}

	return colorTheGrid(m, n)
}
