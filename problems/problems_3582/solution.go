package problem3582

import (
	"encoding/json"
	"log"
	"strings"
)

func generateTag(caption string) string {
	splits := strings.Split(caption, " ")
	var words []string
	start := true
	for _, word := range splits {
		if len(word) == 0 {
			continue
		}
		if start {
			words = append(words, strings.ToLower(word))
			start = false
		} else {
			words = append(words, strings.ToUpper(string(word[0]))+strings.ToLower(word[1:]))
		}
	}
	s := "#" + strings.Join(words, "")
	if len(s) > 100 {
		s = s[:100]
	}
	return s
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var caption string

	if err := json.Unmarshal([]byte(inputValues[0]), &caption); err != nil {
		log.Fatal(err)
	}

	return generateTag(caption)
}
