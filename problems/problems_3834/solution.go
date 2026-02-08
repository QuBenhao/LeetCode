package problem3834

import (
	"encoding/json"
	"log"
	"strings"
)

func mergeAdjacent(nums []int) []int64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return mergeAdjacent(nums)
}
