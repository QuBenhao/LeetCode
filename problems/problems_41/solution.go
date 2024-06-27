package problem41

import (
	"encoding/json"
	"log"
	"strings"
)

func firstMissingPositive(nums []int) int {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(values[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return firstMissingPositive(nums)
}
