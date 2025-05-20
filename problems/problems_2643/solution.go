package problem2643

import (
	"encoding/json"
	"log"
	"strings"
)

func rowAndMaximumOnes(mat [][]int) []int {

}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var mat [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &mat); err != nil {
		log.Fatal(err)
	}

	return rowAndMaximumOnes(mat)
}
