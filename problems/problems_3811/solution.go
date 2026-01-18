package problem3811

import (
	"encoding/json"
	"log"
	"strings"
)

func alternatingXOR(nums []int, target1 int, target2 int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var target1 int
	var target2 int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &target1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &target2); err != nil {
		log.Fatal(err)
	}

	return alternatingXOR(nums, target1, target2)
}
