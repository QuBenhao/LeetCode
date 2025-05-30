package problem909

import (
	"encoding/json"
	"log"
	"strings"
)

func snakesAndLadders(board [][]int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var board [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &board); err != nil {
		log.Fatal(err)
	}

	return snakesAndLadders(board)
}
