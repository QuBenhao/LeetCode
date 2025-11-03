package problem3318

import (
	"encoding/json"
	"log"
	"strings"
)

func findXSum(nums []int, k int, x int) []int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var k int
	var x int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &x); err != nil {
		log.Fatal(err)
	}

	return findXSum(nums, k, x)
}
