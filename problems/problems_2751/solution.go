package problem2751

import (
	"encoding/json"
	"log"
	"strings"
)

func survivedRobotsHealths(positions []int, healths []int, directions string) []int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var positions []int
	var healths []int
	var directions string

	if err := json.Unmarshal([]byte(inputValues[0]), &positions); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &healths); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &directions); err != nil {
		log.Fatal(err)
	}

	return survivedRobotsHealths(positions, healths, directions)
}
