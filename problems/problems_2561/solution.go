package problem2561

import (
	"encoding/json"
	"log"
	"math"
	"slices"
	"strings"
)

func minCost(basket1, basket2 []int) (ans int64) {
	cnt := map[int]int{}
	for i, x := range basket1 {
		cnt[x]++
		cnt[basket2[i]]--
	}

	a := []int{}
	mn := math.MaxInt
	for x, c := range cnt {
		if c%2 != 0 {
			return -1
		}
		mn = min(mn, x)
		for range abs(c) / 2 {
			a = append(a, x)
		}
	}

	slices.Sort(a)

	for _, x := range a[:len(a)/2] {
		ans += int64(min(x, mn*2))
	}
	return
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var basket1 []int
	var basket2 []int

	if err := json.Unmarshal([]byte(inputValues[0]), &basket1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &basket2); err != nil {
		log.Fatal(err)
	}

	return minCost(basket1, basket2)
}
