package problem2929

import (
	"encoding/json"
	"log"
	"strings"
)

func distributeCandies(n int, limit int) int64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var limit int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &limit); err != nil {
		log.Fatal(err)
	}

	return distributeCandies(n, limit)
}
