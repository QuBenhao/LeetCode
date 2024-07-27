package problem699

import (
	"encoding/json"
	"log"
	"strings"
)

func fallingSquares(positions [][]int) []int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var positions [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &positions); err != nil {
		log.Fatal(err)
	}

	return fallingSquares(positions)
}
