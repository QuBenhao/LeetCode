package problem2398

import (
	"encoding/json"
	"log"
	"strings"
)

func maximumRobots(chargeTimes []int, runningCosts []int, budget int64) int {
	n := len(chargeTimes)
	left, right := 0, n
	check := func(length int) bool {
		var s int64
		var q []int
		for i := 0; i < n; i++ {
			for len(q) > 0 && chargeTimes[q[len(q)-1]] <= chargeTimes[i] {
				q = q[:len(q)-1]
			}
			q = append(q, i)
			s += int64(runningCosts[i])
			if i >= q[0]+length {
				q = q[1:]
			}
			if i >= length-1 {
				if s*int64(length)+int64(chargeTimes[q[0]]) <= budget {
					return true
				}
				s -= int64(runningCosts[i-length+1])
			}
		}
		return false
	}
	for left < right {
		mid := left + (right-left+1)/2
		if check(mid) {
			left = mid
		} else {
			right = mid - 1
		}
	}
	return left
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var chargeTimes []int
	var runningCosts []int
	var budget int64

	if err := json.Unmarshal([]byte(inputValues[0]), &chargeTimes); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &runningCosts); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &budget); err != nil {
		log.Fatal(err)
	}

	return maximumRobots(chargeTimes, runningCosts, budget)
}
