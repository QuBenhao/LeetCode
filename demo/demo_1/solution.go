package problem1

import (
	"encoding/json"
	"log"
	"strings"
)

func twoSum(nums []int, target int) []int {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var nums []int
	var target int

	if err := json.Unmarshal([]byte(values[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &target); err != nil {
		log.Fatal(err)
	}

	return twoSum(nums, target)
}
