package problem3184

import (
	"encoding/json"
	"log"
	"strings"
)

func countCompleteDayPairs(hours []int) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var hours []int

	if err := json.Unmarshal([]byte(inputValues[0]), &hours); err != nil {
		log.Fatal(err)
	}

	return countCompleteDayPairs(hours)
}
