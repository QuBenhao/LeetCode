package problem943

import (
	"encoding/json"
	"log"
	"strings"
)

func shortestSuperstring(words []string) string {
	n := len(words)
	g := make([][]int, n)
	for i := range n {
		g[i] = make([]int, n)
		for j := range n {
			if i == j {
				continue
			}
			for k := min(len(words[i]), len(words[j])); k > 0; k-- {
				if strings.HasSuffix(words[i], words[j][:k]) {
					g[i][j] = k
					break
				}
			}
		}
	}
	mask := 1 << n
	dp := make([][]int, mask)
	track := make([][]int, mask)
	for i := range mask {
		dp[i] = make([]int, n)
		track[i] = make([]int, n)
		for j := range n {
			track[i][j] = -1
		}
	}
	for s := range mask {
		for i := range n {
			if ((s >> i) & 1) == 0 {
				continue
			}
			for j := range n {
				if i == j || ((s>>j)&1) == 1 {
					continue
				}
				if ns := s | (1 << j); dp[ns][j] < dp[s][i]+g[i][j] {
					dp[ns][j] = dp[s][i] + g[i][j]
					track[ns][j] = i
				}
			}
		}
	}

	getMax := func(mk int) int {
		idx, m := -1, -1
		for i, v := range dp[mk] {
			if ((mk >> i) & 1) == 0 {
				continue
			}
			if v > m {
				m = v
				idx = i
			}
		}
		return idx
	}
	st := mask - 1
	idx := getMax(st)
	ans := words[idx]
	for st > 0 {
		prev := idx
		st, idx = st^(1<<idx), track[st][idx]
		if idx == -1 {
			idx = getMax(st)
			if idx != -1 {
				ans = words[idx] + ans
			}
		} else {
			ans = words[idx][:len(words[idx])-g[idx][prev]] + ans
		}
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var words []string

	if err := json.Unmarshal([]byte(inputValues[0]), &words); err != nil {
		log.Fatal(err)
	}

	return shortestSuperstring(words)
}
