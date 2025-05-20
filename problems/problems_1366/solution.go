package problem1366

import (
	"cmp"
	"encoding/json"
	"log"
	"maps"
	"slices"
	"strings"
)

func rankTeams(votes []string) string {
	n := len(votes[0])
	counter := map[rune][]int{}
	for _, ch := range votes[0] {
		counter[ch] = make([]int, n)
	}
	for _, vote := range votes {
		for i, ch := range vote {
			counter[ch][i]++
		}
	}
	sorted := slices.SortedFunc(maps.Keys(counter), func(a, b rune) int {
		return cmp.Or(slices.Compare(counter[b], counter[a]), cmp.Compare(a, b))
	})
	return string(sorted)
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var votes []string

	if err := json.Unmarshal([]byte(inputValues[0]), &votes); err != nil {
		log.Fatal(err)
	}

	return rankTeams(votes)
}
