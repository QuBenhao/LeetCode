package problem877

import (
	"encoding/json"
	"log"
	"strings"
)

func stoneGame(piles []int) bool {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var piles []int

	if err := json.Unmarshal([]byte(inputValues[0]), &piles); err != nil {
		log.Fatal(err)
	}

	return stoneGame(piles)
}
