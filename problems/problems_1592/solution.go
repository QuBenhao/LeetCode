package problem1592

import (
	"encoding/json"
	"log"
	"strings"
)

func reorderSpaces(text string) string {
	spaces := 0
	n := len(text)
	var words []string
	start := -1
	for i := range n + 1 {
		if i == n || text[i] == ' ' {
			if start != -1 {
				words = append(words, text[start:i])
				start = -1
			}
			if i < n {
				spaces++
			}
		} else if start == -1 {
			start = i
		}
	}
	m := len(words)
	if m == 1 {
		return words[0] + strings.Repeat(" ", spaces)
	}
	d, r := spaces/(m-1), spaces%(m-1)
	result := strings.Join(words, strings.Repeat(" ", d))
	if r > 0 {
		result += strings.Repeat(" ", r)
	}
	return result
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var text string

	if err := json.Unmarshal([]byte(inputValues[0]), &text); err != nil {
		log.Fatal(err)
	}

	return reorderSpaces(text)
}
