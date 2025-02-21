package problem2209

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumWhiteTiles(floor string, numCarpets int, carpetLen int) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var floor string
	var numCarpets int
	var carpetLen int

	if err := json.Unmarshal([]byte(inputValues[0]), &floor); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &numCarpets); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &carpetLen); err != nil {
		log.Fatal(err)
	}

	return minimumWhiteTiles(floor, numCarpets, carpetLen)
}
