package problem2391

import (
	"encoding/json"
	"log"
	"strings"
)

func garbageCollection(garbage []string, travel []int) int {
	ans := len(garbage[0])
	seen := map[rune]struct{}{}
	for i := len(garbage) - 1; i > 0; i-- {
		g := garbage[i]
		for _, c := range g {
			seen[c] = struct{}{}
		}
		ans += len(g) + travel[i-1]*len(seen)
	}
	return ans
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var garbage []string
	var travel []int

	if err := json.Unmarshal([]byte(values[0]), &garbage); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &travel); err != nil {
		log.Fatal(err)
	}

	return garbageCollection(garbage, travel)
}
