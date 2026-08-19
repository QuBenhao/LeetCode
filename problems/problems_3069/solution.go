package problem3069

import (
	"encoding/json"
	"log"
	"strings"
)

func resultArray(nums []int) []int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return resultArray(nums)
}
