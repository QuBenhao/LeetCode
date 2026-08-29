package problem2948

import (
	"encoding/json"
	"log"
	"strings"
)

func lexicographicallySmallestArray(nums []int, limit int) []int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var limit int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &limit); err != nil {
		log.Fatal(err)
	}

	return lexicographicallySmallestArray(nums, limit)
}
