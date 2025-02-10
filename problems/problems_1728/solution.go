package problem1728

import (
	"encoding/json"
	"log"
	"strings"
)

func canMouseWin(grid []string, catJump int, mouseJump int) bool {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var grid []string
	var catJump int
	var mouseJump int

	if err := json.Unmarshal([]byte(inputValues[0]), &grid); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &catJump); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &mouseJump); err != nil {
		log.Fatal(err)
	}

	return canMouseWin(grid, catJump, mouseJump)
}
