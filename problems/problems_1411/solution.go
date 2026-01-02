package problem1411

import (
	"encoding/json"
	"log"
	"strings"
)

func numOfWays(n int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return numOfWays(n)
}
