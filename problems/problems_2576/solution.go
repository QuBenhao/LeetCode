package problem2576

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func maxNumOfMarkedIndices(nums []int) int {
	sort.Ints(nums)
	left := 0
	for right := (len(nums) + 1) / 2; right < len(nums); right++ {
		if nums[right] >= 2*nums[left] {
			left++
		}
	}
	return left << 1
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return maxNumOfMarkedIndices(nums)
}
