package problem3151

import (
	"encoding/json"
	"log"
	"strings"
)

func isArraySpecial(nums []int) bool {
	last := nums[0] & 1
	for i := 1; i < len(nums); i++ {
		if cur := nums[i] & 1; cur == last {
			return false
		} else {
			last = cur
		}
	}
	return true
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return isArraySpecial(nums)
}
