package problemLCP_40

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func maxmiumScore(cards []int, cnt int) int {
	sort.Slice(cards, func(i, j int) bool {
		return cards[i] > cards[j]
	})
	sum := 0
	for i := 0; i < cnt; i++ {
		sum += cards[i]
	}
	if sum%2 == 0 {
		return sum
	}
	replaceSum := func(x int) int {
		for i := cnt; i < len(cards); i++ {
			if cards[i]%2 != x%2 {
				return sum - x + cards[i]
			}
		}
		return 0
	}
	cur := cards[cnt-1]
	ans := replaceSum(cur)
	for i := cnt - 2; i >= 0; i-- {
		if cards[i]%2 != cur%2 {
			ans = max(ans, replaceSum(cards[i]))
			break
		}
	}
	return ans
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var cards []int
	var cnt int

	if err := json.Unmarshal([]byte(inputValues[0]), &cards); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &cnt); err != nil {
		log.Fatal(err)
	}

	return maxmiumScore(cards, cnt)
}
