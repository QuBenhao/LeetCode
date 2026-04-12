package problem1320

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumDistance(word string) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var word string

	if err := json.Unmarshal([]byte(inputValues[0]), &word); err != nil {
		log.Fatal(err)
	}

	return minimumDistance(word)
}
