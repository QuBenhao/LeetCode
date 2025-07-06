package problem3605

import (
	"encoding/json"
	"log"
	"strings"
)

func minStable(nums []int, maxC int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var maxC int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &maxC); err != nil {
		log.Fatal(err)
	}

	return minStable(nums, maxC)
}
