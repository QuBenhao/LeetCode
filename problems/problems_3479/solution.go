package problem3479

import (
	"encoding/json"
	"log"
	"strings"
)

func numOfUnplacedFruits(fruits []int, baskets []int) int {
    
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
