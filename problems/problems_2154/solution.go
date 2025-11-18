package problem2154

import (
	"encoding/json"
	"log"
	"strings"
)

func findFinalValue(nums []int, original int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var original int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &original); err != nil {
		log.Fatal(err)
	}

	return findFinalValue(nums, original)
}
