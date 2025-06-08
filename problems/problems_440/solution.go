package problem440

import (
	"encoding/json"
	"log"
	"strings"
)

func findKthNumber(n int, k int) int {
	var dfs func(int, int) int
	dfs = func(l int, r int) int {
		if l > n {
			return 0
		}
		return min(r, n) - l + 1 + dfs(l*10, r*10+9)
	}

	cur := 1
	for k > 1 {
		count := dfs(cur, cur)
		if count < k {
			k -= count
			cur++
		} else {
			k--
			cur *= 10
		}
	}
	return cur
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return findKthNumber(n, k)
}
