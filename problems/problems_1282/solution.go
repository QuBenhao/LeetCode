package problem1282

import (
	"encoding/json"
	"log"
	"strings"
)

func groupThePeople(groupSizes []int) (ans [][]int) {
	groups := make(map[int][]int)
	for i, size := range groupSizes {
		groups[size] = append(groups[size], i)
	}
	for sz, group := range groups {
		for i := 0; i < len(group); i += sz {
			ans = append(ans, group[i:i+sz])
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var groupSizes []int

	if err := json.Unmarshal([]byte(inputValues[0]), &groupSizes); err != nil {
		log.Fatal(err)
	}

	return groupThePeople(groupSizes)
}
