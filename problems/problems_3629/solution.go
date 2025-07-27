package problem3629

import (
	"encoding/json"
	"log"
	"strings"
)

func minJumps(nums []int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return minJumps(nums)
}
