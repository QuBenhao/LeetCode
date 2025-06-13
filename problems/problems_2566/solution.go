package problem2566

import (
	"encoding/json"
	"log"
	"strings"
)

func minMaxDifference(num int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var num int

	if err := json.Unmarshal([]byte(inputValues[0]), &num); err != nil {
		log.Fatal(err)
	}

	return minMaxDifference(num)
}
