package problem1848

import (
	"encoding/json"
	"log"
	"strings"
)

func getMinDistance(nums []int, target int, start int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var target int
	var start int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &target); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &start); err != nil {
		log.Fatal(err)
	}

	return getMinDistance(nums, target, start)
}
