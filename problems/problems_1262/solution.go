package problem1262

import (
	"encoding/json"
	"log"
	"strings"
)

func maxSumDivThree(nums []int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return maxSumDivThree(nums)
}
