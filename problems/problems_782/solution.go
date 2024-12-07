package problem782

import (
	"encoding/json"
	"log"
	"strings"
)

func movesToChessboard(board [][]int) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var board [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &board); err != nil {
		log.Fatal(err)
	}

	return movesToChessboard(board)
}
