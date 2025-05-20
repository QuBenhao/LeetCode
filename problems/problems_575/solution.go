package problem575

import (
	"encoding/json"
	"log"
	"strings"
)

func distributeCandies(candyType []int) int {
	set := map[int]struct{}{}
	for _, t := range candyType {
		set[t] = struct{}{}
	}
	return min(len(set), len(candyType)/2)
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var candyType []int

	if err := json.Unmarshal([]byte(values[0]), &candyType); err != nil {
		log.Fatal(err)
	}

	return distributeCandies(candyType)
}
