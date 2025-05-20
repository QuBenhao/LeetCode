package problem2444

import (
	"encoding/json"
	"log"
	"strings"
)

func countSubarrays(nums []int, minK int, maxK int) (ans int64) {
	minLeft, maxLeft, invalid := -1, -1, -1
	for i, num := range nums {
		if num < minK || num > maxK {
			invalid = i
		} else {
			if num == minK {
				minLeft = i
			}
			if num == maxK {
				maxLeft = i
			}
		}
		ans += int64(max(0, min(minLeft, maxLeft)-invalid))
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var minK int
	var maxK int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &minK); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &maxK); err != nil {
		log.Fatal(err)
	}

	return countSubarrays(nums, minK, maxK)
}
