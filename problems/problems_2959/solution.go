package problem2959

import (
	"encoding/json"
	"log"
	"strings"
)

func numberOfSets(n int, maxDistance int, roads [][]int) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var maxDistance int
	var roads [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &maxDistance); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &roads); err != nil {
		log.Fatal(err)
	}

	return numberOfSets(n, maxDistance, roads)
}
