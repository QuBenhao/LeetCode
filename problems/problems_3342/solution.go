package problem3342

import (
	"encoding/json"
	"log"
	"strings"
)

func minTimeToReach(moveTime [][]int) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var moveTime [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &moveTime); err != nil {
		log.Fatal(err)
	}

	return minTimeToReach(moveTime)
}
