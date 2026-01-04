package problem3797

import (
	"encoding/json"
	"log"
	"strings"
)

func numberOfRoutes(grid []string, d int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var grid []string
	var d int

	if err := json.Unmarshal([]byte(inputValues[0]), &grid); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &d); err != nil {
		log.Fatal(err)
	}

	return numberOfRoutes(grid, d)
}
