package problem2071

import (
	"encoding/json"
	"log"
	"strings"
)

func maxTaskAssign(tasks []int, workers []int, pills int, strength int) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var tasks []int
	var workers []int
	var pills int
	var strength int

	if err := json.Unmarshal([]byte(inputValues[0]), &tasks); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &workers); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &pills); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &strength); err != nil {
		log.Fatal(err)
	}

	return maxTaskAssign(tasks, workers, pills, strength)
}
