package problem2786

import (
	"encoding/json"
	"log"
	"strings"
)

func maxScore(nums []int, x int) int64 {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var nums []int
	var x int

	if err := json.Unmarshal([]byte(values[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &x); err != nil {
		log.Fatal(err)
	}

	return maxScore(nums, x)
}
