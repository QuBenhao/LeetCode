package problem1717

import (
	"encoding/json"
	"log"
	"strings"
)

func maximumGain(s string, x int, y int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string
	var x int
	var y int

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &x); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &y); err != nil {
		log.Fatal(err)
	}

	return maximumGain(s, x, y)
}
