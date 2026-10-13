package problem3723

import (
	"encoding/json"
	"log"
	"strings"
)

func maxSumOfSquares(num int, sum int) string {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var num int
	var sum int

	if err := json.Unmarshal([]byte(inputValues[0]), &num); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &sum); err != nil {
		log.Fatal(err)
	}

	return maxSumOfSquares(num, sum)
}
