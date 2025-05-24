package problem2942

import (
	"encoding/json"
	"log"
	"strings"
)

func findWordsContaining(words []string, x byte) (ans []int) {
	for i, word := range words {
		if strings.Contains(word, string(x)) {
			ans = append(ans, i)
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var words []string
	var x byte

	if err := json.Unmarshal([]byte(inputValues[0]), &words); err != nil {
		log.Fatal(err)
	}
	var xStr string
	if err := json.Unmarshal([]byte(inputValues[1]), &xStr); err != nil {
		log.Fatal(err)
	}
	if len(xStr) > 1 {
		x = xStr[1]
	} else {
		x = xStr[0]
	}

	return findWordsContaining(words, x)
}
