package problem139

import (
	"encoding/json"
	"log"
	"strings"
)

func wordBreak(s string, wordDict []string) bool {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string
	var wordDict []string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &wordDict); err != nil {
		log.Fatal(err)
	}

	return wordBreak(s, wordDict)
}
