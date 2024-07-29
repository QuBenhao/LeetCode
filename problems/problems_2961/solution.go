package problem2961

import (
	"encoding/json"
	"log"
	"strings"
)

func getGoodIndices(variables [][]int, target int) []int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var variables [][]int
	var target int

	if err := json.Unmarshal([]byte(inputValues[0]), &variables); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &target); err != nil {
		log.Fatal(err)
	}

	return getGoodIndices(variables, target)
}
