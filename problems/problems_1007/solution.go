package problem1007

import (
	"encoding/json"
	"log"
	"strings"
)

func minDominoRotations(tops []int, bottoms []int) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var tops []int
	var bottoms []int

	if err := json.Unmarshal([]byte(inputValues[0]), &tops); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &bottoms); err != nil {
		log.Fatal(err)
	}

	return minDominoRotations(tops, bottoms)
}
