package problem3192

import (
	"encoding/json"
	"log"
	"strings"
)

func minOperations(nums []int) (ans int) {
	for _, num := range nums {
		if ans%2 == num {
			ans++
		}
	}
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return minOperations(nums)
}
