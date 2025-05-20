package problem1561

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func maxCoins(piles []int) (ans int) {
	sort.Ints(piles)
	n := len(piles)
	for i, j := n-2, 0; j < n/3; j++ {
		ans += piles[i]
		i -= 2
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var piles []int

	if err := json.Unmarshal([]byte(inputValues[0]), &piles); err != nil {
		log.Fatal(err)
	}

	return maxCoins(piles)
}
