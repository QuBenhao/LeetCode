package problem1406

import (
	"encoding/json"
	"log"
	"strings"
)

func stoneGameIII(stoneValue []int) string {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var stoneValue []int

	if err := json.Unmarshal([]byte(inputValues[0]), &stoneValue); err != nil {
		log.Fatal(err)
	}

	return stoneGameIII(stoneValue)
}
