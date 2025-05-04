package problem3537

import (
	"encoding/json"
	"log"
	"strings"
)

func specialGrid(N int) [][]int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var N int

	if err := json.Unmarshal([]byte(inputValues[0]), &N); err != nil {
		log.Fatal(err)
	}

	return specialGrid(N)
}
