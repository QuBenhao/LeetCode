package problem3418

import (
	"encoding/json"
	"log"
	"strings"
)

func maximumAmount(coins [][]int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var coins [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &coins); err != nil {
		log.Fatal(err)
	}

	return maximumAmount(coins)
}
