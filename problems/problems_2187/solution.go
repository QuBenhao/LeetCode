package problem2187

import (
	"encoding/json"
	"log"
	"slices"
	"strings"
)

func minimumTime(time []int, totalTrips int) int64 {
	minT := slices.Min(time)
	maxT := slices.Max(time)
	avg := (totalTrips-1)/len(time) + 1
	// Loop invariant: check(left) is always false
	left := minT*avg - 1
	// Loop invariant: check(right) is always true
	right := min(maxT*avg, minT*totalTrips)
	for left+1 < right { // The open interval (left, right) is nonempty
		mid := (left + right) / 2
		sum := 0
		for _, t := range time {
			sum += mid / t
		}
		if sum >= totalTrips {
			right = mid // Shrink the binary-search interval to (left, mid)
		} else {
			left = mid // Shrink the binary-search interval to (mid, right)
		}
	}
	// Now left equals right-1
	// check(left) = false and check(right) = true, so the answer is right
	return int64(right) // The smallest value for which the predicate is true
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var time []int
	var totalTrips int

	if err := json.Unmarshal([]byte(inputValues[0]), &time); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &totalTrips); err != nil {
		log.Fatal(err)
	}

	return minimumTime(time, totalTrips)
}
