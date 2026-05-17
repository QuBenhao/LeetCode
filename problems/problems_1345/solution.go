package problem1345

import (
	"encoding/json"
	"log"
	"strings"
)

func minJumps(arr []int) int {
	n := len(arr)
	connected := make(map[int][]int)
	for i, v := range arr {
		connected[v] = append(connected[v], i)
	}
	dp := make([]int, n)
	for i := range n {
		dp[i] = n + 5
	}
	dp[0] = 0
	q := []int{0}
	for len(q) > 0 {
		cur := q[0]
		q = q[1:]
		for _, nxt := range connected[arr[cur]] {
			if dp[nxt] <= dp[cur]+1 {
				continue
			}
			dp[nxt] = dp[cur] + 1
			q = append(q, nxt)
		}
		delete(connected, arr[cur])
		for _, d := range []int{-1, 1} {
			nxt := cur + d
			if nxt < 0 || nxt == n || dp[nxt] <= dp[cur]+1 {
				continue
			}
			dp[nxt] = dp[cur] + 1
			q = append(q, nxt)
		}
	}
	return dp[n-1]
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var arr []int

	if err := json.Unmarshal([]byte(inputValues[0]), &arr); err != nil {
		log.Fatal(err)
	}

	return minJumps(arr)
}
