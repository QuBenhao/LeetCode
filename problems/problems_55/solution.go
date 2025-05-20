package problem55

import (
	"encoding/json"
	"log"
	"strings"
)

func canJump(nums []int) bool {
	maxDis := 0
	for i, v := range nums {
		maxDis = max(maxDis, i+v)
		if maxDis >= len(nums)-1 {
			return true
		}
		if i >= maxDis {
			return false
		}
	}
	return false
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return canJump(nums)
}
