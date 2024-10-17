package problem3193

import (
	"encoding/json"
	"log"
	"strings"
)

func numberOfPermutations(n int, requirements [][]int) int {
	const mod = 1_000_000_007
	req := make([]int, n)
	for i := 1; i < n; i++ {
		req[i] = -1
	}
	for _, p := range requirements {
		req[p[0]] = p[1]
	}
	if req[0] > 0 {
		return 0
	}

	m := slices.Max(req)
	f := make([]int, m+1)
	f[0] = 1
	for i := 1; i < n; i++ {
		mx := m
		if req[i] >= 0 {
			mx = req[i]
		}
		if r := req[i-1]; r >= 0 {
			clear(f[:r])
			for j := r + 1; j <= min(i+r, mx); j++ {
				f[j] = f[r]
			}
			clear(f[min(i+r, mx)+1:])
		} else {
			for j := 1; j <= mx; j++ { // 计算前缀和
				f[j] = (f[j] + f[j-1]) % mod
			}
			for j := mx; j > i; j-- { // 计算子数组和
				f[j] = (f[j] - f[j-i-1] + mod) % mod
			}
		}
	}
	return f[req[n-1]]
}


func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var requirements [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &requirements); err != nil {
		log.Fatal(err)
	}

	return numberOfPermutations(n, requirements)
}
