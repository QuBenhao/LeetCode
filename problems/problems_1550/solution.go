package problem1550

import (
	"encoding/json"
	"log"
	"strings"
)

func threeConsecutiveOdds(arr []int) bool {
	count := 0
	for i, num := range arr {
		if num%2 == 1 {
			count++
		} else {
			count = 0
		}
		if i >= 2 && count == 3 {
			return true
		}
	}
	return false
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var arr []int

	if err := json.Unmarshal([]byte(inputValues[0]), &arr); err != nil {
		log.Fatal(err)
	}

	return threeConsecutiveOdds(arr)
}
