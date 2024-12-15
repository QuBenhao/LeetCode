package problem1847

import (
	"encoding/json"
	"log"
	"strings"
)

func closestRoom(rooms [][]int, queries [][]int) []int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var rooms [][]int
	var queries [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &rooms); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &queries); err != nil {
		log.Fatal(err)
	}

	return closestRoom(rooms, queries)
}
