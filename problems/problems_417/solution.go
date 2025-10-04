package problem417

import (
	"encoding/json"
	"log"
	"strings"
)

func pacificAtlantic(heights [][]int) [][]int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var heights [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &heights); err != nil {
		log.Fatal(err)
	}

	return pacificAtlantic(heights)
}
