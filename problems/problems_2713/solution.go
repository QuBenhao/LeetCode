package problem2713

import (
	"encoding/json"
	"log"
	"strings"
)

func maxIncreasingCells(mat [][]int) int {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var mat [][]int

	if err := json.Unmarshal([]byte(values[0]), &mat); err != nil {
		log.Fatal(err)
	}

	return maxIncreasingCells(mat)
}
