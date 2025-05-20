package problem1953

import (
	"encoding/json"
	"log"
	"slices"
	"strings"
)

func numberOfWeeks(milestones []int) int64 {
	s := 0
	for _, x := range milestones {
		s += x
	}
	m := slices.Max(milestones)
	if m > s-m+1 {
		return int64((s-m)*2 + 1)
	}
	return int64(s)
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var milestones []int

	if err := json.Unmarshal([]byte(values[0]), &milestones); err != nil {
		log.Fatal(err)
	}

	return numberOfWeeks(milestones)
}
