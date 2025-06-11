package problem3423

import (
	"encoding/json"
	"log"
	"strings"
)

func maxAdjacentDistance(nums []int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return maxAdjacentDistance(nums)
}
