package problem1014

import (
	"encoding/json"
	"log"
	"strings"
)

func maxScoreSightseeingPair(values []int) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var values []int

	if err := json.Unmarshal([]byte(inputValues[0]), &values); err != nil {
		log.Fatal(err)
	}

	return maxScoreSightseeingPair(values)
}
