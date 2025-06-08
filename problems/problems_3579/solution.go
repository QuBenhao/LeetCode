package problem3579

import (
	"encoding/json"
	"log"
	"math"
	"strings"
)

func minOperations(word1 string, word2 string) int {
	update := func(c map[int]int, a, b byte, o int) int {
		if a == b {
			return o
		}
		if h := int(a-'a') + 26*int(b-'a'); c[h] > 0 {
			c[h]--
			return o
		} else {
			c[26*int(a-'a')+int(b-'a')]++
			return o + 1
		}
	}

	n := len(word1)

	revOp := make([][]int, n)
	for i := range n {
		revOp[i] = make([]int, n)
	}
	for i := range 2*n - 1 {
		l, r := i/2, (i+1)/2
		cnt, op := map[int]int{}, 1
		for l >= 0 && r < n {
			op = update(cnt, word1[l], word2[r], op)
			if l != r {
				op = update(cnt, word1[r], word2[l], op)
			}
			revOp[l][r] = op
			l--
			r++
		}
	}

	dp := make([]int, n+1)
	for i := range n {
		cur := math.MaxInt
		cnt, op := map[int]int{}, 0
		for j := i; j >= 0; j-- {
			op = update(cnt, word1[j], word2[j], op)
			cur = min(cur, dp[j]+min(revOp[j][i], op))
		}
		dp[i+1] = cur
	}
	return dp[n]
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var word1 string
	var word2 string

	if err := json.Unmarshal([]byte(inputValues[0]), &word1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &word2); err != nil {
		log.Fatal(err)
	}

	return minOperations(word1, word2)
}
