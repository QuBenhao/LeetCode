package problem3101

import (
	"encoding/json"
	"log"
	"strings"
)

func countAlternatingSubarrays(nums []int) int64 {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return countAlternatingSubarrays(nums)
}
