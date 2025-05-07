package problem1552

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func maxDistance(position []int, m int) int {
	helper := func(d int) bool {
		count, last := 0, -d
		for _, p := range position {
			if p-last >= d {
				count++
				last = p
			}
		}
		return count >= m
	}

	sort.Ints(position)
	left, right := 1, position[len(position)-1]-position[0]
	for left < right {
		mid := left + (right-left+1)/2
		if helper(mid) {
			left = mid
		} else {
			right = mid - 1
		}
	}
	return left
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var position []int
	var m int

	if err := json.Unmarshal([]byte(inputValues[0]), &position); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &m); err != nil {
		log.Fatal(err)
	}

	return maxDistance(position, m)
}
