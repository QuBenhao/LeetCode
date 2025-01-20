package problem2218

import (
	"encoding/json"
	"log"
	"strings"
)

func maxValueOfCoins(piles [][]int, k int) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var piles [][]int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &piles); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return maxValueOfCoins(piles, k)
}
