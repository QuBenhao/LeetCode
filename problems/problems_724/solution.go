package problem724

import (
	"encoding/json"
	"log"
	"strings"
)

func pivotIndex(nums []int) int {
	s := 0
	for _, num := range nums {
		s += num
	}
	leftSum := 0
	for i, num := range nums {
		s -= num
		if leftSum == s {
			return i
		}
		leftSum += num
	}
	return -1
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return pivotIndex(nums)
}
