package problem1970

import (
	"encoding/json"
	"log"
	"strings"
)

func latestDayToCross(row int, col int, cells [][]int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var row int
	var col int
	var cells [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &row); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &col); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &cells); err != nil {
		log.Fatal(err)
	}

	return latestDayToCross(row, col, cells)
}
