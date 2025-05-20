package problem1450

import (
	"encoding/json"
	"log"
	"strings"
)

func busyStudent(startTime []int, endTime []int, queryTime int) (ans int) {
	for i := 0; i < len(startTime); i++ {
		if startTime[i] <= queryTime && queryTime <= endTime[i] {
			ans++
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var startTime []int
	var endTime []int
	var queryTime int

	if err := json.Unmarshal([]byte(inputValues[0]), &startTime); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &endTime); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &queryTime); err != nil {
		log.Fatal(err)
	}

	return busyStudent(startTime, endTime, queryTime)
}
