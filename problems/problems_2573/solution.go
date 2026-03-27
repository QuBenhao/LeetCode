package problem2573

import (
	"encoding/json"
	"log"
	"strings"
)

func findTheString(lcp [][]int) string {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var lcp [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &lcp); err != nil {
		log.Fatal(err)
	}

	return findTheString(lcp)
}
