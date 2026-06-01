package problem3633

import (
	"encoding/json"
	"log"
	"strings"
)

func earliestFinishTime(landStartTime []int, landDuration []int, waterStartTime []int, waterDuration []int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var landStartTime []int
	var landDuration []int
	var waterStartTime []int
	var waterDuration []int

	if err := json.Unmarshal([]byte(inputValues[0]), &landStartTime); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &landDuration); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &waterStartTime); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &waterDuration); err != nil {
		log.Fatal(err)
	}

	return earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration)
}
