package problem2207

import (
	"encoding/json"
	"log"
	"strings"
)

func maximumSubsequenceCount(text string, pattern string) int64 {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var text string
	var pattern string

	if err := json.Unmarshal([]byte(inputValues[0]), &text); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &pattern); err != nil {
		log.Fatal(err)
	}

	return maximumSubsequenceCount(text, pattern)
}
