package problem3296

import (
	"encoding/json"
	"log"
	"strings"
)

func minNumberOfSeconds(mountainHeight int, workerTimes []int) int64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var mountainHeight int
	var workerTimes []int

	if err := json.Unmarshal([]byte(inputValues[0]), &mountainHeight); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &workerTimes); err != nil {
		log.Fatal(err)
	}

	return minNumberOfSeconds(mountainHeight, workerTimes)
}
