package problem3609

import (
	"encoding/json"
	"log"
	"strings"
)

func minMoves(sx int, sy int, tx int, ty int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var sx int
	var sy int
	var tx int
	var ty int

	if err := json.Unmarshal([]byte(inputValues[0]), &sx); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &sy); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &tx); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &ty); err != nil {
		log.Fatal(err)
	}

	return minMoves(sx, sy, tx, ty)
}
