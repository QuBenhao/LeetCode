package problem1014

import (
	"encoding/json"
	"log"
	"strings"
)

func maxScoreSightseeingPair(values []int) (ans int) {
	left := values[0]
	for i := 1; i < len(values); i++ {
		ans = max(ans, left+values[i]-i)
		left = max(left, values[i]+i)
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var values []int

	if err := json.Unmarshal([]byte(inputValues[0]), &values); err != nil {
		log.Fatal(err)
	}

	return maxScoreSightseeingPair(values)
}
