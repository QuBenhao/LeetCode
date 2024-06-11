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

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var str [][]string

	if err := json.Unmarshal([]byte(values[0]), &str); err != nil {
		log.Fatal(err)
	}

	board := make([][]byte, len(str))
	for i := 0; i < len(board); i++ {
		board[i] = make([]byte, len(str[i]))
		for j := 0; j < len(board[i]); j++ {
			board[i][j] = str[i][j][0]
		}
	}

	return countBattleships(board)
}
