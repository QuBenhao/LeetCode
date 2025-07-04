package problem1394

import (
	"encoding/json"
	"log"
	"strings"
)

func findLucky(arr []int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var arr []int

	if err := json.Unmarshal([]byte(inputValues[0]), &arr); err != nil {
		log.Fatal(err)
	}

	return findLucky(arr)
}
