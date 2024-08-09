package problem2940

import (
	"encoding/json"
	"log"
	"strings"
)

func leftmostBuildingQueries(heights []int, queries [][]int) []int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var heights []int
	var queries [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &heights); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &queries); err != nil {
		log.Fatal(err)
	}

	return leftmostBuildingQueries(heights, queries)
}
