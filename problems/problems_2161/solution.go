package problem2161

import (
	"encoding/json"
	"log"
	"strings"
)

func pivotArray(nums []int, pivot int) []int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var pivot int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &pivot); err != nil {
		log.Fatal(err)
	}

	return pivotArray(nums, pivot)
}
