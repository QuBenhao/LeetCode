package problem1760

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumSize(nums []int, maxOperations int) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var maxOperations int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &maxOperations); err != nil {
		log.Fatal(err)
	}

	return minimumSize(nums, maxOperations)
}
