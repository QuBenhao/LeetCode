package problem2588

import (
	"encoding/json"
	"log"
	"strings"
)

func beautifulSubarrays(nums []int) int64 {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return beautifulSubarrays(nums)
}
