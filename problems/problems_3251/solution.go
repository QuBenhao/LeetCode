package problem3251

import (
	"encoding/json"
	"log"
	"strings"
)

func countOfPairs(nums []int) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return countOfPairs(nums)
}
