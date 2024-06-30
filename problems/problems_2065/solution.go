package problem2065

import (
	"encoding/json"
	"log"
	"strings"
)

func maximalPathQuality(values []int, edges [][]int, maxTime int) int {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var values []int
	var edges [][]int
	var maxTime int

	if err := json.Unmarshal([]byte(values[0]), &values); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &edges); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[2]), &maxTime); err != nil {
		log.Fatal(err)
	}

	return maximalPathQuality(values, edges, maxTime)
}
