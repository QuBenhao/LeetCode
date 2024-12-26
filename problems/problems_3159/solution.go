package problem3159

import (
	"encoding/json"
	"log"
	"strings"
)

func occurrencesOfElement(nums []int, queries []int, x int) []int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var queries []int
	var x int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &queries); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &x); err != nil {
		log.Fatal(err)
	}

	return occurrencesOfElement(nums, queries, x)
}
