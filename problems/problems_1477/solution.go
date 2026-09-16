package problem1477

import (
	"encoding/json"
	"log"
	"strings"
)

func minSumOfLengths(arr []int, target int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var arr []int
	var target int

	if err := json.Unmarshal([]byte(inputValues[0]), &arr); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &target); err != nil {
		log.Fatal(err)
	}

	return minSumOfLengths(arr, target)
}
