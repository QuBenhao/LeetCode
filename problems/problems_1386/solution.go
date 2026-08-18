package problem1386

import (
	"encoding/json"
	"log"
	"strings"
)

func maxNumberOfFamilies(n int, reservedSeats [][]int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var reservedSeats [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &reservedSeats); err != nil {
		log.Fatal(err)
	}

	return maxNumberOfFamilies(n, reservedSeats)
}
