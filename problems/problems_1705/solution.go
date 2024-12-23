package problem1705

import (
	"encoding/json"
	"log"
	"strings"
)

func eatenApples(apples []int, days []int) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var apples []int
	var days []int

	if err := json.Unmarshal([]byte(inputValues[0]), &apples); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &days); err != nil {
		log.Fatal(err)
	}

	return eatenApples(apples, days)
}
