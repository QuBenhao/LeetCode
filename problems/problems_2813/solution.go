package problem2813

import (
	"encoding/json"
	"log"
	"slices"
	"strings"
)

func findMaximumElegance(items [][]int, k int) int64 {
	slices.SortFunc(items, func(a, b []int) int {
		return b[0] - a[0]
	})
	ans, totalProfit := 0, 0
	vis := map[int]bool{}
	var duplicate []int
	for i, item := range items {
		profit, category := item[0], item[1]
		if i < k {
			totalProfit += profit
			if !vis[category] {
				vis[category] = true
			} else {
				duplicate = append(duplicate, profit)
			}
		} else if len(duplicate) > 0 && !vis[category] {
			vis[category] = true
			totalProfit += profit - duplicate[len(duplicate)-1]
			duplicate = duplicate[:len(duplicate)-1]
		}
		ans = max(ans, totalProfit+len(vis)*len(vis))
	}
	return int64(ans)
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var items [][]int
	var k int

	if err := json.Unmarshal([]byte(values[0]), &items); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &k); err != nil {
		log.Fatal(err)
	}

	return findMaximumElegance(items, k)
}
