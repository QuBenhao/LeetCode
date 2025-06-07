package problem3575

import (
	"encoding/json"
	"log"
	"strings"
)

func goodSubtreeSum(vals []int, par []int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var vals []int
	var par []int

	if err := json.Unmarshal([]byte(inputValues[0]), &vals); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &par); err != nil {
		log.Fatal(err)
	}

	return goodSubtreeSum(vals, par)
}
