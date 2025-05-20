package problem422

import (
	"encoding/json"
	"log"
	"strings"
)

func validWordSquare(words []string) bool {
	for i, word := range words {
		if len(word) > len(words) {
			return false
		}
		for j := 0; j < len(word); j++ {
			if (len(word) <= j) != (len(words[j]) <= i) {
				return false
			} else if len(word) > j && word[j] != words[j][i] {
				return false
			}
		}
	}
	return true
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var words []string

	if err := json.Unmarshal([]byte(values[0]), &words); err != nil {
		log.Fatal(err)
	}

	return validWordSquare(words)
}
