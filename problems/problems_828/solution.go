package problem828

import (
	"encoding/json"
	"log"
	"strings"
)

func uniqueLetterString(s string) (ans int) {
	n := len(s)
	charIndices := make(map[rune][]int)
	for i, r := range s {
		charIndices[r] = append(charIndices[r], i)
	}
	for _, indices := range charIndices {
		m := len(indices)
		if m == 0 {
			continue
		}
		if m == 1 {
			ans += (indices[0] + 1) * (n - indices[0])
			continue
		}
		for i := range indices {
			switch i {
			case 0:
				ans += (indices[i] + 1) * (indices[i+1] - indices[i])
			case m - 1:
				ans += (n - indices[i]) * (indices[i] - indices[i-1])
			default:
				ans += (indices[i] - indices[i-1]) * (indices[i+1] - indices[i])
			}
		}
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return uniqueLetterString(s)
}
