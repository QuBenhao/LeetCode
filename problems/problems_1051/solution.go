package problem1051

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func heightChecker(heights []int) (ans int) {
	expected := make([]int, len(heights))
	copy(expected, heights)
	sort.Ints(expected)
	for i := 0; i < len(heights); i++ {
		if heights[i] != expected[i] {
			ans++
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var heights []int

	if err := json.Unmarshal([]byte(inputValues[0]), &heights); err != nil {
		log.Fatal(err)
	}

	return heightChecker(heights)
}
