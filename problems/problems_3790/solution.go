package problem3790

import (
	"encoding/json"
	"log"
	"strings"
)

func minAllOneMultiple(k int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &k); err != nil {
		log.Fatal(err)
	}

	return minAllOneMultiple(k)
}
