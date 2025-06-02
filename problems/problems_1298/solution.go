package problem1298

import (
	"encoding/json"
	"log"
	"strings"
)

func maxCandies(status []int, candies []int, keys [][]int, containedBoxes [][]int, initialBoxes []int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var status []int
	var candies []int
	var keys [][]int
	var containedBoxes [][]int
	var initialBoxes []int

	if err := json.Unmarshal([]byte(inputValues[0]), &status); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &candies); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &keys); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &containedBoxes); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[4]), &initialBoxes); err != nil {
		log.Fatal(err)
	}

	return maxCandies(status, candies, keys, containedBoxes, initialBoxes)
}
