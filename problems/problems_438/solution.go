package problem438

import (
	"encoding/json"
	"log"
	"strings"
)

func findAnagrams(s string, p string) (ans []int) {
	helper := func(counter []int, key int, val int) int {
		before := counter[key] == 0
		counter[key] += val
		if before {
			return 1
		} else if counter[key] == 0 {
			return -1
		}
		return 0
	}

	counter := make([]int, 26)
	for _, c := range p {
		counter[c-'a']--
	}
	diff := 0
	for _, c := range counter {
		if c != 0 {
			diff++
		}
	}
	for i, c := range s {
		diff += helper(counter, int(c-'a'), 1)
		if i >= len(p)-1 {
			if diff == 0 {
				ans = append(ans, i-len(p)+1)
			}
			diff += helper(counter, int(s[i-len(p)+1]-'a'), -1)
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string
	var p string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &p); err != nil {
		log.Fatal(err)
	}

	return findAnagrams(s, p)
}
