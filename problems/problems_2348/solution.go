package problem2348

import (
	"encoding/json"
	"log"
	"strings"
)

func zeroFilledSubarray(nums []int) int64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return zeroFilledSubarray(nums)
}
