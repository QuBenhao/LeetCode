package problem2644

import (
	"encoding/json"
	"log"
	"strings"
)

func maxDivScore(nums []int, divisors []int) int {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var nums []int
	var divisors []int

	if err := json.Unmarshal([]byte(values[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &divisors); err != nil {
		log.Fatal(err)
	}

	return maxDivScore(nums, divisors)
}
