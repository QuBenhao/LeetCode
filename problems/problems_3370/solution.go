package problem3370

import (
	"encoding/json"
	"log"
	"strings"
)

func smallestNumber(n int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return smallestNumber(n)
}
