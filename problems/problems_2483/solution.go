package problem2483

import (
	"encoding/json"
	"log"
	"strings"
)

func bestClosingTime(customers string) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var customers string

	if err := json.Unmarshal([]byte(inputValues[0]), &customers); err != nil {
		log.Fatal(err)
	}

	return bestClosingTime(customers)
}
