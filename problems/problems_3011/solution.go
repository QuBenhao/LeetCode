package problem3011

import (
	"encoding/json"
	"log"
	"math/bits"
	"strings"
)

func canSortArray(nums []int) bool {
	for i, preMax, n := 0, 0, len(nums); i < n; {
		ones := bits.OnesCount32(uint32(uint(nums[i])))
		curMax := nums[i]
		for ; i < n && bits.OnesCount32(uint32(uint(nums[i]))) == ones; i++ {
			if nums[i] < preMax {
				return false
			}
			curMax = max(curMax, nums[i])
		}
		preMax = curMax
	}
	return true
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return canSortArray(nums)
}
