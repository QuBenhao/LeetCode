package problem1356

import (
	"encoding/json"
	"log"
	"strings"
)

func sortByBits(arr []int) []int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var arr []int

	if err := json.Unmarshal([]byte(inputValues[0]), &arr); err != nil {
		log.Fatal(err)
	}

	return sortByBits(arr)
}
