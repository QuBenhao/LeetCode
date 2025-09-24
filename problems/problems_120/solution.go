package problem120

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumTotal(triangle [][]int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var triangle [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &triangle); err != nil {
		log.Fatal(err)
	}

	return minimumTotal(triangle)
}
