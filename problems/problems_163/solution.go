package problem163

import (
	"encoding/json"
	"log"
	"strings"
)

func findMissingRanges(nums []int, lower int, upper int) [][]int {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var nums []int
	var lower int
	var upper int

	if err := json.Unmarshal([]byte(values[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &lower); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[2]), &upper); err != nil {
		log.Fatal(err)
	}

	return findMissingRanges(nums, lower, upper)
}
