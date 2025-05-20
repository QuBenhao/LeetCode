package problem57

import (
	"encoding/json"
	"log"
	"strings"
)

func insert(intervals [][]int, newInterval []int) (ans [][]int) {
	left, right := newInterval[0], newInterval[1]
	for _, interval := range intervals {
		a, b := interval[0], interval[1]
		if b < left || a > right {
			if a > right {
				ans = append(ans, []int{left, right})
				left = 0x3f3f3f
				right = 0x3f3f3f
			}
			ans = append(ans, interval)
		} else {
			left = min(left, a)
			right = max(right, b)
		}
	}
	if left != 0x3f3f3f && (len(ans) == 0 || ans[len(ans)-1][1] < left) {
		ans = append(ans, []int{left, right})
	}
	return
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var intervals [][]int
	var newInterval []int

	if err := json.Unmarshal([]byte(values[0]), &intervals); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &newInterval); err != nil {
		log.Fatal(err)
	}

	return insert(intervals, newInterval)
}
