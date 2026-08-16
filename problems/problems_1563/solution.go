package problem1563

import (
	"encoding/json"
	"log"
	"strings"
)

func stoneGameV(stoneValue []int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var stoneValue []int

	if err := json.Unmarshal([]byte(inputValues[0]), &stoneValue); err != nil {
		log.Fatal(err)
	}

	return stoneGameV(stoneValue)
}
