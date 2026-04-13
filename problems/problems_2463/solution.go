package problem2463

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumTotalDistance(robot []int, factory [][]int) int64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var robot []int
	var factory [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &robot); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &factory); err != nil {
		log.Fatal(err)
	}

	return minimumTotalDistance(robot, factory)
}
