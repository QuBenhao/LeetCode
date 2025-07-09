package problem3440

import (
	"encoding/json"
	"log"
	"strings"
)

func maxFreeTime(eventTime int, startTime []int, endTime []int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var eventTime int
	var startTime []int
	var endTime []int

	if err := json.Unmarshal([]byte(inputValues[0]), &eventTime); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &startTime); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &endTime); err != nil {
		log.Fatal(err)
	}

	return maxFreeTime(eventTime, startTime, endTime)
}
