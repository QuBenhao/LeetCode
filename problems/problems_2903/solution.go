package problem2903

import (
	"encoding/json"
	"log"
	"strings"
)

func findIndices(nums []int, indexDifference, valueDifference int) []int {
	maxIdx, minIdx := 0, 0
	for j := indexDifference; j < len(nums); j++ {
		i := j - indexDifference
		if nums[i] > nums[maxIdx] {
			maxIdx = i
		} else if nums[i] < nums[minIdx] {
			minIdx = i
		}
		if nums[maxIdx]-nums[j] >= valueDifference {
			return []int{maxIdx, j}
		}
		if nums[j]-nums[minIdx] >= valueDifference {
			return []int{minIdx, j}
		}
	}
	return []int{-1, -1}
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var nums []int
	var indexDifference int
	var valueDifference int

	if err := json.Unmarshal([]byte(values[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &indexDifference); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[2]), &valueDifference); err != nil {
		log.Fatal(err)
	}

	return findIndices(nums, indexDifference, valueDifference)
}
