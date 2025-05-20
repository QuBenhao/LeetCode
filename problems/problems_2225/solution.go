package problem2225

import (
	"encoding/json"
	"log"
	"slices"
	"strings"
)

func findWinners(matches [][]int) [][]int {
	loseTimes := map[int]int{}
	for _, match := range matches {
		win, lose := match[0], match[1]
		if loseTimes[win] == 0 {
			loseTimes[win] = 0
		}
		loseTimes[lose]++
	}
	ans := make([][]int, 2)
	for k, v := range loseTimes {
		if v < 2 {
			ans[v] = append(ans[v], k)
		}
	}
	slices.Sort(ans[0])
	slices.Sort(ans[1])
	return ans
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var matches [][]int

	if err := json.Unmarshal([]byte(values[0]), &matches); err != nil {
		log.Fatal(err)
	}

	return findWinners(matches)
}
