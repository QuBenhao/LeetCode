package problem3592

import (
	"encoding/json"
	"log"
	"strings"
)

func findCoins(numWays []int) []int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var numWays []int

	if err := json.Unmarshal([]byte(inputValues[0]), &numWays); err != nil {
		log.Fatal(err)
	}

	return findCoins(numWays)
}
