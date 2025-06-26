package problem2014

import (
	"encoding/json"
	"log"
	"strings"
)

func longestSubsequenceRepeatedK(s string, k int) string {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return longestSubsequenceRepeatedK(s, k)
}
