package problemLCR_073

import (
	"encoding/json"
	"log"
	"strings"
)

func minEatingSpeed(piles []int, h int) int {
	helper := func(k int) bool {
		count := 0
		for _, pile := range piles {
			count += (pile + k - 1) / k
		}
		return count <= h
	}
	left, right := 1, int(1e9)
	for left < right {
		mid := left + (right-left-1)/2
		if helper(mid) {
			right = mid
		} else {
			left = mid + 1
		}
	}
	return left
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var piles []int
	var h int

	if err := json.Unmarshal([]byte(inputValues[0]), &piles); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &h); err != nil {
		log.Fatal(err)
	}

	return minEatingSpeed(piles, h)
}
