package problemInterview_16__06

import (
	"encoding/json"
	"log"
	"strings"
)

func smallestDifference(a []int, b []int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var a []int
	var b []int

	if err := json.Unmarshal([]byte(inputValues[0]), &a); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &b); err != nil {
		log.Fatal(err)
	}

	return smallestDifference(a, b)
}
