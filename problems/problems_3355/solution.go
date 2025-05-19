package problem3355

import (
	"encoding/json"
	"log"
	"strings"
)

func isZeroArray(nums []int, queries [][]int) bool {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var queries [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &queries); err != nil {
		log.Fatal(err)
	}

	return isZeroArray(nums, queries)
}
