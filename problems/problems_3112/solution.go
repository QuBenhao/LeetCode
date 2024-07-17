package problem3112

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumTime(n int, edges [][]int, disappear []int) []int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var edges [][]int
	var disappear []int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &edges); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &disappear); err != nil {
		log.Fatal(err)
	}

	return minimumTime(n, edges, disappear)
}
