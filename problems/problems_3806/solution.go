package problem3806

import (
	"encoding/json"
	"log"
	"strings"
)

func maximumAND(nums []int, k int, m int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var k int
	var m int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &m); err != nil {
		log.Fatal(err)
	}

	return maximumAND(nums, k, m)
}
