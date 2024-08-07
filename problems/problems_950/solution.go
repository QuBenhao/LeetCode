package problem950

import (
	"encoding/json"
	"log"
	"slices"
	"sort"
	"strings"
)

func deckRevealedIncreasing(deck []int) []int {
	sort.Ints(deck)
	ans := make([]int, 0, len(deck))
	for len(deck) > 0 {
		if len(ans) > 0 {
			ans = append(ans, ans[0])
			ans = ans[1:]
		}
		ans = append(ans, deck[len(deck)-1])
		deck = deck[:len(deck)-1]
	}
	slices.Reverse(ans)
	return ans
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var deck []int

	if err := json.Unmarshal([]byte(inputValues[0]), &deck); err != nil {
		log.Fatal(err)
	}

	return deckRevealedIncreasing(deck)
}
