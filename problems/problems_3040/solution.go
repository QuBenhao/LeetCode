package problem3040

import (
	"encoding/json"
	"log"
	"strings"
)

func maxOperations(nums []int) int {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(values[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return maxOperations(nums)
}
