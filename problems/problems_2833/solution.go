package problem2833

import (
	"encoding/json"
	"log"
	"strings"
)

func furthestDistanceFromOrigin(moves string) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var moves string

	if err := json.Unmarshal([]byte(inputValues[0]), &moves); err != nil {
		log.Fatal(err)
	}

	return furthestDistanceFromOrigin(moves)
}
