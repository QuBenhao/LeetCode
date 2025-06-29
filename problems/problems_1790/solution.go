package problem1790

import (
	"encoding/json"
	"log"
	"strings"
)

func areAlmostEqual(s1 string, s2 string) bool {
	d1, d2 := -1, -1
	for i := range len(s1) {
		if s1[i] != s2[i] {
			if d1 == -1 {
				d1 = i
			} else if d2 == -1 {
				d2 = i
			} else {
				return false
			}
		}
	}
	if d1 == -1 {
		return true
	}
	if d2 == -1 {
		return false
	}
	return s1[d1] == s2[d2] && s1[d2] == s2[d1]
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s1 string
	var s2 string

	if err := json.Unmarshal([]byte(inputValues[0]), &s1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &s2); err != nil {
		log.Fatal(err)
	}

	return areAlmostEqual(s1, s2)
}
