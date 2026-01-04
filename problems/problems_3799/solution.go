package problem3799

import (
	"encoding/json"
	"log"
	"strings"
)

func wordSquares(words []string) [][]string {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var words []string

	if err := json.Unmarshal([]byte(inputValues[0]), &words); err != nil {
		log.Fatal(err)
	}

	return wordSquares(words)
}
