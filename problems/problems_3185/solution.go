package problem3185

import (
	"encoding/json"
	"log"
	"strings"
)

func countCompleteDayPairs(hours []int) int64 {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var hours []int

	if err := json.Unmarshal([]byte(inputValues[0]), &hours); err != nil {
		log.Fatal(err)
	}

	return countCompleteDayPairs(hours)
}
