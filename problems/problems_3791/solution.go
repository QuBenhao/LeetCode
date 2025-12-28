package problem3791

import (
	"encoding/json"
	"log"
	"strings"
)

func countBalanced(low int64, high int64) int64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var low int64
	var high int64

	if err := json.Unmarshal([]byte(inputValues[0]), &low); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &high); err != nil {
		log.Fatal(err)
	}

	return countBalanced(low, high)
}
