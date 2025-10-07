package problem2300

import (
	"encoding/json"
	"log"
	"strings"
)

func successfulPairs(spells []int, potions []int, success int64) []int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var spells []int
	var potions []int
	var success int64

	if err := json.Unmarshal([]byte(inputValues[0]), &spells); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &potions); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &success); err != nil {
		log.Fatal(err)
	}

	return successfulPairs(spells, potions, success)
}
