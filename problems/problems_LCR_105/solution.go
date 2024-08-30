package problemLCR_105

import (
	"encoding/json"
	"log"
	"strings"
)

func maxAreaOfIsland(grid [][]int) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var grid [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &grid); err != nil {
		log.Fatal(err)
	}

	return maxAreaOfIsland(grid)
}
