package problem874

import (
	"encoding/json"
	"log"
	"strings"
)

func robotSim(commands []int, obstacles [][]int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var commands []int
	var obstacles [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &commands); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &obstacles); err != nil {
		log.Fatal(err)
	}

	return robotSim(commands, obstacles)
}
