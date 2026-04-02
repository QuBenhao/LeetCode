package problem3661

import (
	"encoding/json"
	"log"
	"strings"
)

func maxWalls(robots []int, distance []int, walls []int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var robots []int
	var distance []int
	var walls []int

	if err := json.Unmarshal([]byte(inputValues[0]), &robots); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &distance); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &walls); err != nil {
		log.Fatal(err)
	}

	return maxWalls(robots, distance, walls)
}
