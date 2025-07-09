package problem3440

import (
	"encoding/json"
	"log"
	"strings"
)

func maxFreeTime(eventTime int, startTime []int, endTime []int) (ans int) {
	n := len(startTime)
	distances := make([]int, n+1)
	distances[0] = startTime[0]
	for i := 1; i < n; i++ {
		distances[i] = startTime[i] - endTime[i-1]
	}
	distances[n] = eventTime - endTime[n-1]
	a, b, c := -1, -1, -1
	for i := 0; i <= n; i++ {
		if a == -1 || distances[i] >= distances[a] {
			a, b, c = i, a, b
		} else if b == -1 || distances[i] >= distances[b] {
			b, c = i, b
		} else if c == -1 || distances[i] > distances[c] {
			c = i
		}
	}

	getMax := func(idx int) int {
		if a != idx && a != idx+1 {
			return distances[a]
		}
		if b != idx && b != idx+1 {
			return distances[b]
		}
		return distances[c]
	}

	for i := range n {
		if cur := endTime[i] - startTime[i]; getMax(i) >= cur {
			ans = max(ans, distances[i]+distances[i+1]+cur)
		} else {
			ans = max(ans, distances[i]+distances[i+1])
		}
	}

	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var eventTime int
	var startTime []int
	var endTime []int

	if err := json.Unmarshal([]byte(inputValues[0]), &eventTime); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &startTime); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &endTime); err != nil {
		log.Fatal(err)
	}

	return maxFreeTime(eventTime, startTime, endTime)
}
