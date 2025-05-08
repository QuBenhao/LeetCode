package problem1760

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumSize(nums []int, maxOperations int) int {
	helper := func(mx int) bool {
		op := 0
		for _, num := range nums {
			if num > mx {
				op += (num - 1) / mx
				if op > maxOperations {
					return true
				}
			}
		}
		return false
	}
	left, right := 1, int(1e9)
	for left < right {
		mid := left + (right-left)/2
		if helper(mid) {
			left = mid + 1
		} else {
			right = mid
		}
	}
	return left
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var maxOperations int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &maxOperations); err != nil {
		log.Fatal(err)
	}

	return minimumSize(nums, maxOperations)
}
