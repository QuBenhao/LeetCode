package problem999

import (
	"encoding/json"
	"log"
	"strings"
)

func numRookCaptures(board [][]byte) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var board [][]byte

	var boardStr [][]string
	if err := json.Unmarshal([]byte(inputValues[0]), &boardStr); err != nil {
		log.Fatal(err)
	}
	board = make([][]byte, len(boardStr))
	for i := 0; i < len(board); i++ {
		board[i] = make([]byte, len(boardStr[i]))
		for j := 0; j < len(board[i]); j++ {
			board[i][j] = boardStr[i][j][0]
		}
	}

	return numRookCaptures(board)
}
