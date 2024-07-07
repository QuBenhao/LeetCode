package problem35

import (
	"encoding/json"
	"log"
	"strings"
)

func searchInsert(nums []int, target int) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var target int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &target); err != nil {
		log.Fatal(err)
	}

	return searchInsert(nums, target)
}
