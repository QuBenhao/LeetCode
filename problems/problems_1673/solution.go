package problem1673

import (
	"encoding/json"
	"log"
	"strings"
)

func mostCompetitive(nums []int, k int) []int {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var nums []int
	var k int

	if err := json.Unmarshal([]byte(values[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &k); err != nil {
		log.Fatal(err)
	}

	return mostCompetitive(nums, k)
}
