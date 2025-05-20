package problem419

import (
	"encoding/json"
	"log"
	"strings"
)

func countBattleships(board [][]byte) (ans int) {
	for i, row := range board {
		for j, r := range row {
			if r == 'X' && (i == 0 || board[i-1][j] != 'X') && (j == 0 || board[i][j-1] != 'X') {
				ans++
			}
		}
	}
	return
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var board [][]byte

	var boardStr [][]string
	if err := json.Unmarshal([]byte(values[0]), &boardStr); err != nil {
		log.Fatal(err)
	}
	board = make([][]byte, len(boardStr))
	for i := 0; i < len(board); i++ {
		board[i] = make([]byte, len(boardStr[i]))
		for j := 0; j < len(board[i]); j++ {
			board[i][j] = boardStr[i][j][0]
		}
	}

	return countBattleships(board)
}
