package problem40

import (
	"encoding/json"
	"log"
	"strings"
)

func combinationSum2(candidates []int, target int) [][]int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var candidates []int
	var target int

	if err := json.Unmarshal([]byte(inputValues[0]), &candidates); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &target); err != nil {
		log.Fatal(err)
	}

	return combinationSum2(candidates, target)
}
