package problem3439

import (
	"encoding/json"
	"log"
	"strings"
)

func maxFreeTime(eventTime int, k int, startTime []int, endTime []int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var eventTime int
	var k int
	var startTime []int
	var endTime []int

	if err := json.Unmarshal([]byte(inputValues[0]), &eventTime); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &startTime); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &endTime); err != nil {
		log.Fatal(err)
	}

	return maxFreeTime(eventTime, k, startTime, endTime)
}
