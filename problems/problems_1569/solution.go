package problem1569

import (
	"encoding/json"
	"log"
	"strings"
)

func numOfWays(nums []int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return numOfWays(nums)
}
