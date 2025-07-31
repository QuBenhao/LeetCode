package problem436

import (
	"encoding/json"
	"log"
	"slices"
	"strings"
)

func findRightInterval(intervals [][]int) []int {
	n := len(intervals)
	indexMap := make(map[int]int)
	for i, interval := range intervals {
		indexMap[interval[0]] = i
	}
	slices.SortFunc(intervals, func(a, b []int) int {
		return a[0] - b[0]
	})
	result := make([]int, n)
	for _, interval := range intervals {
		left, right := 0, n
		for left < right {
			mid := left + (right-left)/2
			if intervals[mid][0] < interval[1] {
				left = mid + 1
			} else {
				right = mid
			}
		}
		if left < n {
			result[indexMap[interval[0]]] = indexMap[intervals[left][0]]
		} else {
			result[indexMap[interval[0]]] = -1
		}
	}
	return result
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var intervals [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &intervals); err != nil {
		log.Fatal(err)
	}

	return findRightInterval(intervals)
}
