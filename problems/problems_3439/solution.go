package problem3439

import (
	"encoding/json"
	"log"
	"strings"
)

func maxFreeTime(eventTime int, k int, startTime []int, endTime []int) (ans int) {
	n := len(startTime)
	getDistance := func(idx int) int {
		if idx == 0 {
			return startTime[0]
		}
		if idx == n {
			return eventTime - endTime[n-1]
		}
		return startTime[idx] - endTime[idx-1]
	}
	cur := 0
	for i := range k + 1 {
		cur += getDistance(i)
	}
	ans = cur
	for i := k + 1; i <= n; i++ {
		cur += getDistance(i) - getDistance(i-k-1)
		ans = max(ans, cur)
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var eventTime int
	var k int
	var startTime []int
	var endTime []int

	if err := json.Unmarshal([]byte(inputValues[0]), &eventTime); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &startTime); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &endTime); err != nil {
		log.Fatal(err)
	}

	return maxFreeTime(eventTime, k, startTime, endTime)
}
