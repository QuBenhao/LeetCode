package problem3330

import (
	"encoding/json"
	"log"
	"strings"
)

func possibleStringCount(word string) (ans int) {
	ans++
	for i := range len(word) - 1 {
		if word[i] == word[i+1] {
			ans++
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var word string

	if err := json.Unmarshal([]byte(inputValues[0]), &word); err != nil {
		log.Fatal(err)
	}

	return possibleStringCount(word)
}
