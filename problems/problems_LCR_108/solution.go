package problemLCR_108

import (
	"encoding/json"
	"log"
	"strings"
)

func ladderLength(beginWord string, endWord string, wordList []string) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var beginWord string
	var endWord string
	var wordList []string

	if err := json.Unmarshal([]byte(inputValues[0]), &beginWord); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &endWord); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &wordList); err != nil {
		log.Fatal(err)
	}

	return ladderLength(beginWord, endWord, wordList)
}
