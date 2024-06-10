package problem1768

import (
	"encoding/json"
	"log"
	"strings"
)

func mergeAlternately(word1 string, word2 string) string {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var word1 string
	var word2 string

	if err := json.Unmarshal([]byte(values[0]), &word1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &word2); err != nil {
		log.Fatal(err)
	}

	return mergeAlternately(word1, word2)
}
