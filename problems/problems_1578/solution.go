package problem1578

import (
	"encoding/json"
	"log"
	"strings"
)

func minCost(colors string, neededTime []int) (ans int) {
	n := len(colors)
	for i, j := 0, 0; i < n-1; i = j {
		for j = i + 1; j < n && colors[j] == colors[i]; j++ {
			if neededTime[i] < neededTime[j] {
				ans += neededTime[i]
				i = j
			} else {
				ans += neededTime[j]
			}
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var colors string
	var neededTime []int

	if err := json.Unmarshal([]byte(inputValues[0]), &colors); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &neededTime); err != nil {
		log.Fatal(err)
	}

	return minCost(colors, neededTime)
}
