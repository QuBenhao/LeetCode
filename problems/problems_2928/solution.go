package problem2928

import (
	"encoding/json"
	"log"
	"strings"
)

func combinationTwo(n int) int {
	if n <= 1 {
		return 0
	}
	return n * (n - 1) / 2
}

func distributeCandies(n int, limit int) int {
	return combinationTwo(n+2) - 3*combinationTwo(n+1-limit) + 3*combinationTwo(n-2*limit) - combinationTwo(n-1-3*limit)
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var n int
	var limit int

	if err := json.Unmarshal([]byte(values[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &limit); err != nil {
		log.Fatal(err)
	}

	return distributeCandies(n, limit)
}
