package problem1432

import (
	"encoding/json"
	"log"
	"strings"
)

func maxDiff(num int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var num int

	if err := json.Unmarshal([]byte(inputValues[0]), &num); err != nil {
		log.Fatal(err)
	}

	return maxDiff(num)
}
