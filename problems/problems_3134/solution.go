package problem3134

import (
	"encoding/json"
	"log"
	"strings"
)

func medianOfUniquenessArray(nums []int) int {
	n := len(nums)
	k := ((n*(n+1))/2 + 1) / 2

	check := func(mid int) bool {
		freq := map[int]int{}
		count, l := 0, 0
		for r, num := range nums {
			freq[num]++
			for len(freq) > mid {
				freq[nums[l]]--
				if freq[nums[l]] == 0 {
					delete(freq, nums[l])
				}
				l++
			}
			count += r - l + 1
		}
		if count >= k {
			return true
		}
		return false
	}

	left, right := 1, n
	for left < right {
		mid := left + (right-left)/2
		if check(mid) {
			right = mid
		} else {
			left = mid + 1
		}
	}
	return left
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return medianOfUniquenessArray(nums)
}
