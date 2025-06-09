package problem3442

import (
	"encoding/json"
	"log"
	"strings"
)

func maxDifference(s string) int {
	maxOdd, minEven := 0, len(s)
	counts := make([]int, 26)
	for _, c := range s {
		counts[c-'a']++
	}
	for _, v := range counts {
		if v == 0 {
			continue
		}
		if v%2 == 1 {
			maxOdd = max(maxOdd, v)
		} else {
			minEven = min(minEven, v)
		}
	}
	return maxOdd - minEven
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return maxDifference(s)
}
