package problem1488

import (
	"encoding/json"
	"log"
	"strings"
)

func avoidFlood(rains []int) []int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var rains []int

	if err := json.Unmarshal([]byte(inputValues[0]), &rains); err != nil {
		log.Fatal(err)
	}

	return avoidFlood(rains)
}
