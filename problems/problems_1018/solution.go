package problem1018

import (
	"encoding/json"
	"log"
	"strings"
)

func prefixesDivBy5(nums []int) []bool {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return prefixesDivBy5(nums)
}
