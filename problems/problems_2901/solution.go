package problem2901

import (
	"encoding/json"
	"log"
	"strings"
)

func getWordsInLongestSubsequence(words []string, groups []int) []string {

}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var words []string
	var groups []int

	if err := json.Unmarshal([]byte(inputValues[0]), &words); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &groups); err != nil {
		log.Fatal(err)
	}

	return getWordsInLongestSubsequence(words, groups)
}
