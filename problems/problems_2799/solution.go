package problem2799

import (
	"encoding/json"
	"log"
	"strings"
)

func countCompleteSubarrays(nums []int) (ans int) {
	uniques := make(map[int]struct{})
	for _, num := range nums {
		uniques[num] = struct{}{}
	}
	uniquesCount := len(uniques)
	window := make(map[int]int)
	right, n := 0, len(nums)
	for _, num := range nums {
		for right < n && len(window) < uniquesCount {
			window[nums[right]]++
			right++
		}
		if len(window) == uniquesCount {
			ans += n - right + 1
		}
		window[num]--
		if window[num] == 0 {
			delete(window, num)
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

	return countCompleteSubarrays(nums)
}
