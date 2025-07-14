package problem3136

import (
	"encoding/json"
	"log"
	"strings"
)

func isValid(word string) bool {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var word string

	if err := json.Unmarshal([]byte(inputValues[0]), &word); err != nil {
		log.Fatal(err)
	}

	return isValid(word)
}
