package problem3664

import (
	"encoding/json"
	"log"
	"strings"
)

func score(cards []string, x byte) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var cards []string
	var x byte

	if err := json.Unmarshal([]byte(inputValues[0]), &cards); err != nil {
		log.Fatal(err)
	}
	var xStr string
	if err := json.Unmarshal([]byte(inputValues[1]), &xStr); err != nil {
		log.Fatal(err)
	}
	if len(xStr) > 1 {
		x = xStr[1]
	} else {
		x = xStr[0]
	}

	return score(cards, x)
}
