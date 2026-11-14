package problem3364

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumSumSubarray(nums []int, l int, r int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var l int
	var r int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &l); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &r); err != nil {
		log.Fatal(err)
	}

	return minimumSumSubarray(nums, l, r)
}
