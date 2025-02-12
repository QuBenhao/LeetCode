package problem1742

import (
	"encoding/json"
	"log"
	"strings"
)

func countBalls(lowLimit int, highLimit int) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var lowLimit int
	var highLimit int

	if err := json.Unmarshal([]byte(inputValues[0]), &lowLimit); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &highLimit); err != nil {
		log.Fatal(err)
	}

	return countBalls(lowLimit, highLimit)
}
