package problem1298

import (
	"encoding/json"
	"log"
	"strings"
)

func maxCandies(status []int, candies []int, keys [][]int, containedBoxes [][]int, initialBoxes []int) int {
	boxes := map[int]bool{}
	hasKeys := map[int]bool{}
	q := []int{}
	for _, box := range initialBoxes {
		if status[box] == 1 {
			q = append(q, box)
		} else {
			boxes[box] = true
		}
	}
	totalCandies := 0
	for len(q) > 0 {
		box := q[0]
		q = q[1:]
		for _, key := range keys[box] {
			hasKeys[key] = true
			if boxes[key] {
				q = append(q, key)
				boxes[key] = false
			}
		}
		totalCandies += candies[box]
		for _, containedBox := range containedBoxes[box] {
			if status[containedBox] == 1 || hasKeys[containedBox] {
				q = append(q, containedBox)
			} else {
				boxes[containedBox] = true
			}
		}
	}
	return totalCandies
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
