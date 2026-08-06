package problem3348

import (
	"encoding/json"
	"log"
	"strings"
)

func smallestNumber(num string, t int64) string {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var num string
	var t int64

	if err := json.Unmarshal([]byte(inputValues[0]), &num); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &t); err != nil {
		log.Fatal(err)
	}

	return smallestNumber(num, t)
}
