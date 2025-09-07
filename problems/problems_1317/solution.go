package problem1317

import (
	"encoding/json"
	"log"
	"strings"
)

func getNoZeroIntegers(n int) []int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return getNoZeroIntegers(n)
}
