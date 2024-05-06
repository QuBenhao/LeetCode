package problem1463

import (
	"encoding/json"
	"log"
	"strings"
)

func Solve(input string) int {
	values := strings.Split(input, "\n")
	var grid [][]int

	if err := json.Unmarshal([]byte(values[0]), &grid); err != nil {
		log.Fatal(err)
	}

	return cherryPickup(grid)
}

func cherryPickup(grid [][]int) int {

}