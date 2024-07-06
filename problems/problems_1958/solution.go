package problem1958

import (
	"encoding/json"
	"log"
	"strings"
)

func checkMove(board [][]byte, rMove int, cMove int, color byte) bool {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var board [][]byte
	var rMove int
	var cMove int
	var color byte

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
	if err := json.Unmarshal([]byte(inputValues[1]), &rMove); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &cMove); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &color); err != nil {
		log.Fatal(err)
	}

	return checkMove(board, rMove, cMove, color)
}
