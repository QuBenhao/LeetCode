package problem997

import (
	"encoding/json"
	"log"
	"strings"
)

func findJudge(n int, trust [][]int) int {
	counter := make([]int, n+1)
	for _, t := range trust {
		counter[t[0]]--
		counter[t[1]]++
	}
	for i := 1; i <= n; i++ {
		if counter[i] == n-1 {
			return i
		}
	}
	return -1
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var trust [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &trust); err != nil {
		log.Fatal(err)
	}

	return findJudge(n, trust)
}
