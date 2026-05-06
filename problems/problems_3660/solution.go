package problem3660

import (
	"encoding/json"
	"log"
	"strings"
)

func maxValue(nums []int) []int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return maxValue(nums)
}
