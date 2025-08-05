package problem3477

import (
	"encoding/json"
	"log"
	"strings"
)

func numOfUnplacedFruits(fruits []int, baskets []int) (ans int) {
	for _, fruit := range fruits {
		placed := false
		for i, basket := range baskets {
			if basket >= fruit {
				baskets[i] = 0
				placed = true
				break
			}
		}
		if !placed {
			ans++
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var fruits []int
	var baskets []int

	if err := json.Unmarshal([]byte(inputValues[0]), &fruits); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &baskets); err != nil {
		log.Fatal(err)
	}

	return numOfUnplacedFruits(fruits, baskets)
}
