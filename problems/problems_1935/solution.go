package problem1935

import (
	"encoding/json"
	"log"
	"strings"
)

func canBeTypedWords(text string, brokenLetters string) (ans int) {
	for _, t := range strings.Split(text, " ") {
		if !strings.ContainsAny(t, brokenLetters) {
			ans++
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var text string
	var brokenLetters string

	if err := json.Unmarshal([]byte(inputValues[0]), &text); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &brokenLetters); err != nil {
		log.Fatal(err)
	}

	return canBeTypedWords(text, brokenLetters)
}
