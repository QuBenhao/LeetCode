package problem1625

import (
	"encoding/json"
	"log"
	"strings"
)

func findLexSmallestString(s string, a int, b int) string {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string
	var a int
	var b int

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &a); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &b); err != nil {
		log.Fatal(err)
	}

	return findLexSmallestString(s, a, b)
}
