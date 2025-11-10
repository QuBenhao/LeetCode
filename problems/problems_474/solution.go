package problem474

import (
	"encoding/json"
	"log"
	"strings"
)

func findMaxForm(strs []string, m int, n int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var strs []string
	var m int
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &strs); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &m); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &n); err != nil {
		log.Fatal(err)
	}

	return findMaxForm(strs, m, n)
}
