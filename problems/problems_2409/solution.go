package problem2409

import (
	"encoding/json"
	"log"
	"strings"
)

func countDaysTogether(arriveAlice string, leaveAlice string, arriveBob string, leaveBob string) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var arriveAlice string
	var leaveAlice string
	var arriveBob string
	var leaveBob string

	if err := json.Unmarshal([]byte(inputValues[0]), &arriveAlice); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &leaveAlice); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &arriveBob); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &leaveBob); err != nil {
		log.Fatal(err)
	}

	return countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob)
}
