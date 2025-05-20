package problem3067

import (
	"encoding/json"
	"log"
	"strings"
)

func countPairsOfConnectableServers(edges [][]int, signalSpeed int) []int {
	n := len(edges) + 1
	type edge struct{ to, wt int }
	g := make([][]edge, n)
	for _, e := range edges {
		x, y, wt := e[0], e[1], e[2]
		g[x] = append(g[x], edge{y, wt})
		g[y] = append(g[y], edge{x, wt})
	}

	ans := make([]int, n)
	for i, gi := range g {
		if len(gi) == 1 {
			continue
		}
		var cnt int
		var dfs func(int, int, int)
		dfs = func(x, fa, sum int) {
			if sum%signalSpeed == 0 {
				cnt++
			}
			for _, e := range g[x] {
				if e.to != fa {
					dfs(e.to, x, sum+e.wt)
				}
			}
			return
		}
		sum := 0
		for _, e := range gi {
			cnt = 0
			dfs(e.to, i, e.wt)
			ans[i] += cnt * sum
			sum += cnt
		}
	}
	return ans
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var edges [][]int
	var signalSpeed int

	if err := json.Unmarshal([]byte(values[0]), &edges); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &signalSpeed); err != nil {
		log.Fatal(err)
	}

	return countPairsOfConnectableServers(edges, signalSpeed)
}
