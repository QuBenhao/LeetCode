package problem498

import (
	"encoding/json"
	"log"
	"strings"
)

func findDiagonalOrder(mat [][]int) []int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var mat [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &mat); err != nil {
		log.Fatal(err)
	}

	return findDiagonalOrder(mat)
}
