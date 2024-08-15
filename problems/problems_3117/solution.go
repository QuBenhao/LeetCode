package problem3117

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumValueSum(nums []int, andValues []int) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var andValues []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &andValues); err != nil {
		log.Fatal(err)
	}

	return minimumValueSum(nums, andValues)
}
