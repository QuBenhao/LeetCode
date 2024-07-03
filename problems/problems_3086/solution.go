package problem3086

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumMoves(nums []int, k int, maxChanges int) int64 {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var k int
	var maxChanges int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &maxChanges); err != nil {
		log.Fatal(err)
	}

	return minimumMoves(nums, k, maxChanges)
}
