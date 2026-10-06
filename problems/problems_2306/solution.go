package problem2306

import (
	"encoding/json"
	"log"
	"strings"
)

func distinctNames(ideas []string) (ans int64) {
	group := [26]map[string]bool{}
	for i := range group {
		group[i] = map[string]bool{}
	}
	for _, s := range ideas {
		group[s[0]-'a'][s[1:]] = true // Group by first letter
	}

	for i, a := range group { // Enumerate all pairs of groups
		for _, b := range group[:i] {
			m := 0 // Size of the intersection
			for s := range a {
				if b[s] {
					m++
				}
			}
			ans += int64(len(a)-m) * int64(len(b)-m)
		}
	}
	return ans * 2 // Multiply by 2 at the end
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var ideas []string

	if err := json.Unmarshal([]byte(inputValues[0]), &ideas); err != nil {
		log.Fatal(err)
	}

	return distinctNames(ideas)
}
