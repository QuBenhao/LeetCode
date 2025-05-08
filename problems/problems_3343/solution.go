package problem3343

import (
	"encoding/json"
	"log"
	"strings"
)

func countBalancedPermutations(num string) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var num string

	if err := json.Unmarshal([]byte(inputValues[0]), &num); err != nil {
		log.Fatal(err)
	}

	return countBalancedPermutations(num)
}
