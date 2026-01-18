package problem3809

import (
	"encoding/json"
	"log"
	"strings"
)

func bestTower(towers [][]int, center []int, radius int) []int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var towers [][]int
	var center []int
	var radius int

	if err := json.Unmarshal([]byte(inputValues[0]), &towers); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &center); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &radius); err != nil {
		log.Fatal(err)
	}

	return bestTower(towers, center, radius)
}
