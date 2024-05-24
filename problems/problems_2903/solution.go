package problem2903

import (
	"encoding/json"
	"log"
	"strings"
)

func findIndices(nums []int, indexDifference int, valueDifference int) []int {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var nums []int
	var indexDifference int
	var valueDifference int

	if err := json.Unmarshal([]byte(values[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &indexDifference); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[2]), &valueDifference); err != nil {
		log.Fatal(err)
	}

	return findIndices(nums, indexDifference, valueDifference)
}
