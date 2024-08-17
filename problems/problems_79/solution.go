package problem79

import (
	"encoding/json"
	"log"
	"strings"
)

func exist(board [][]byte, word string) bool {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var board [][]byte
	var word string

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
	if err := json.Unmarshal([]byte(inputValues[1]), &word); err != nil {
		log.Fatal(err)
	}

	return exist(board, word)
}
