package problem3615

import (
	"encoding/json"
	"log"
	"strings"
)

func maxLen(n int, edges [][]int, label string) int {
	graph := make([][]int, n)
	for _, edge := range edges {
		graph[edge[0]] = append(graph[edge[0]], edge[1])
		graph[edge[1]] = append(graph[edge[1]], edge[0])
	}

	maxN := 1 << n
	dp := make([][][]int, n)
	for i := range n {
		dp[i] = make([][]int, n)
		for j := range n {
			dp[i][j] = make([]int, maxN)
			for k := range maxN {
				dp[i][j][k] = -1
			}
		}
	}

	var dfs func(int, int, int) int
	dfs = func(x int, y int, explored int) (maxLen int) {
		if dp[x][y][explored] != -1 {
			return dp[x][y][explored]
		}
		for _, nx := range graph[x] {
			if ((explored >> nx) & 1) != 0 {
				continue
			}
			for _, ny := range graph[y] {
				if ny == nx || ((explored>>ny)&1) != 0 || label[nx] != label[ny] {
					continue
				}
				if nx > ny {
					maxLen = max(maxLen, dfs(ny, nx, explored|(1<<nx)|(1<<ny))+2)
				} else {
					maxLen = max(maxLen, dfs(nx, ny, explored|(1<<nx)|(1<<ny))+2)
				}
			}
		}
		dp[x][y][explored] = maxLen
		return
	}

	ans := 1
	for i := range n {
		ans = max(ans, dfs(i, i, 1<<i)+1)
		for _, j := range graph[i] {
			if j < i || label[i] != label[j] {
				continue
			}
			ans = max(ans, dfs(i, j, (1<<i)|(1<<j))+2)
		}
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var edges [][]int
	var label string

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &edges); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &label); err != nil {
		log.Fatal(err)
	}

	return maxLen(n, edges, label)
}
