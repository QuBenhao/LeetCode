package problem3480

import (
	"encoding/json"
	"log"
	"strings"
)

func maxSubarrays(n int, conflictingPairs [][]int) (ans int64) {
	g0 := make([]int, n+1)
	g1 := make([]int, n+1)
	for i := range g0 {
		g0[i] = n + 1
		g1[i] = n + 1
	}
	for _, pair := range conflictingPairs {
		a, b := pair[0], pair[1]
		if a > b {
			a, b = b, a
		}
		if b < g0[a] {
			g1[a] = g0[a]
			g0[a] = b
		} else if b < g1[a] {
			g1[a] = b
		}
	}
	var extra, maxExtra int64
	b0, b1 := n+1, n+1
	for i := n; i > 0; i-- {
		preB := b0
		b, c := g0[i], g1[i]
		if b < b0 {
			b1 = min(b0, c)
			b0 = b
		} else if b < b1 {
			b1 = b
		} else if c < b1 {
			b1 = c
		}
		ans += int64(b0 - i)
		if b0 != preB {
			extra = 0
		}
		extra += int64(b1 - b0)
		maxExtra = max(maxExtra, extra)
	}
	ans += maxExtra
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var conflictingPairs [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &conflictingPairs); err != nil {
		log.Fatal(err)
	}

	return maxSubarrays(n, conflictingPairs)
}
