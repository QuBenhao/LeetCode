package problem2616

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func minimizeMax(nums []int, p int) int {
	sort.Ints(nums)
	n := len(nums)

	check := func(mid int) bool {
		count := 0
		for i := 0; i < n-1; i++ {
			if nums[i+1]-nums[i] <= mid {
				count++
				i++ // Skip the next element as it's paired with the current one
			}
			if count >= p {
				return true
			}
		}
		return false
	}
	low, high := 0, nums[n-1]-nums[0]
	for low < high {
		mid := low + (high-low)/2
		if check(mid) {
			high = mid // Try for a smaller maximum difference
		} else {
			low = mid + 1 // Increase the minimum difference
		}
	}
	return low
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var p int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &p); err != nil {
		log.Fatal(err)
	}

	return minimizeMax(nums, p)
}
