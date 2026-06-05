package problem2574

import (
	"encoding/json"
	"log"
	"strings"
)

func leftRightDifference(nums []int) []int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return leftRightDifference(nums)
}
