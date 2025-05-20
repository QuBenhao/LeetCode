package problem3297

import (
	"encoding/json"
	"log"
	"strings"
)

func validSubstringCount(word1 string, word2 string) int64 {

}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var word1 string
	var word2 string

	if err := json.Unmarshal([]byte(inputValues[0]), &word1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &word2); err != nil {
		log.Fatal(err)
	}

	return validSubstringCount(word1, word2)
}
