package problem1722

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumHammingDistance(source []int, target []int, allowedSwaps [][]int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var source []int
	var target []int
	var allowedSwaps [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &source); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &target); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &allowedSwaps); err != nil {
		log.Fatal(err)
	}

	return minimumHammingDistance(source, target, allowedSwaps)
}
