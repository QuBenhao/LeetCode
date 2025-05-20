package problem1338

import (
	"encoding/json"
	"log"
	"maps"
	"slices"
	"strings"
)

func minSetSize(arr []int) int {
	counter := map[int]int{}
	for _, num := range arr {
		counter[num]++
	}
	cnt := slices.SortedFunc(maps.Values(counter), func(a, b int) int { return b - a })
	s := 0
	for i, c := range cnt {
		s += c
		if s >= len(arr)/2 {
			return i + 1
		}
	}
	return -1
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var arr []int

	if err := json.Unmarshal([]byte(inputValues[0]), &arr); err != nil {
		log.Fatal(err)
	}

	return minSetSize(arr)
}
