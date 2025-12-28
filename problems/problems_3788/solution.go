package problem3788

import (
	"encoding/json"
	"log"
	"strings"
)

func maximumScore(nums []int) int64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return maximumScore(nums)
}
