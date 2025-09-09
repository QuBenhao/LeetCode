package problem1733

import (
	"encoding/json"
	"log"
	"slices"
	"strings"
)

func minimumTeachings(n int, languages [][]int, friendships [][]int) int {
	m := len(languages)
	lang := make([][]bool, m)
	for i := range lang {
		lang[i] = make([]bool, n)
	}
	for i, language := range languages {
		for _, l := range language {
			lang[i][l-1] = true
		}
	}

	needs := make(map[int]any)
	for _, friendship := range friendships {
		u, v := friendship[0]-1, friendship[1]-1
		has_common := false
		for i := range n {
			if lang[u][i] && lang[v][i] {
				has_common = true
				break
			}
		}
		if has_common {
			continue
		}
		needs[u] = nil
		needs[v] = nil
	}

	if len(needs) == 0 {
		return 0
	}

	counts := make([]int, n)
	for k := range needs {
		for l, ok := range lang[k] {
			if ok {
				counts[l]++
			}
		}
	}
	return len(needs) - slices.Max(counts)
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var languages [][]int
	var friendships [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &languages); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &friendships); err != nil {
		log.Fatal(err)
	}

	return minimumTeachings(n, languages, friendships)
}
