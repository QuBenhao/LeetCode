package problem1552

import (
	"encoding/json"
	"log"
	"strings"
)

func maxDistance(position []int, m int) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var position []int
	var m int

	if err := json.Unmarshal([]byte(inputValues[0]), &position); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &m); err != nil {
		log.Fatal(err)
	}

	return maxDistance(position, m)
}
