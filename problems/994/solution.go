package problem994

import (
	"encoding/json"
	"log"
	"strings"
)

func orangesRotting(grid [][]int) int {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var grid [][]int

	if err := json.Unmarshal([]byte(values[0]), &grid); err != nil {
		log.Fatal(err)
	}

	return orangesRotting(grid)
}
