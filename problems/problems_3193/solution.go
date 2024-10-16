package problem3193

import (
	"encoding/json"
	"log"
	"strings"
)

func numberOfPermutations(n int, requirements [][]int) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var requirements [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &requirements); err != nil {
		log.Fatal(err)
	}

	return numberOfPermutations(n, requirements)
}
