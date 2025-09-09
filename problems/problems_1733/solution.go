package problem1733

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumTeachings(n int, languages [][]int, friendships [][]int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var languages [][]int
	var friendships [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &languages); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &friendships); err != nil {
		log.Fatal(err)
	}

	return minimumTeachings(n, languages, friendships)
}
