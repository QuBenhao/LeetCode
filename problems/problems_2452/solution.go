package problem2452

import (
	"encoding/json"
	"log"
	"strings"
)

func twoEditWords(queries []string, dictionary []string) []string {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var queries []string
	var dictionary []string

	if err := json.Unmarshal([]byte(inputValues[0]), &queries); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &dictionary); err != nil {
		log.Fatal(err)
	}

	return twoEditWords(queries, dictionary)
}
