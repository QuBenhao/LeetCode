package problem2300

import (
	"encoding/json"
	"log"
	"slices"
	"strings"
)

func successfulPairs(spells []int, potions []int, success int64) []int {
	n := len(spells)
	ans := make([]int, n)
	mx := slices.Max(potions)
	counts := make([]int, mx+1)
	for _, p := range potions {
		counts[p]++
	}
	for i := mx - 1; i >= 0; i-- {
		counts[i] += counts[i+1]
	}
	for i, s := range spells {
		low := (success-1)/int64(s) + 1
		if low > int64(mx) {
			continue
		}
		ans[i] = counts[int(low)]
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var spells []int
	var potions []int
	var success int64

	if err := json.Unmarshal([]byte(inputValues[0]), &spells); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &potions); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &success); err != nil {
		log.Fatal(err)
	}

	return successfulPairs(spells, potions, success)
}
