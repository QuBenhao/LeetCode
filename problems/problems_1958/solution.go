package problem1958

import (
	"encoding/json"
	"log"
	"strings"
)

func checkMove(board [][]byte, rMove int, cMove int, color byte) bool {
	m, n := len(board), len(board[0])
	directions := [][]int{{0, 1}, {1, 1}, {1, 0}, {-1, 1}, {1, -1}, {0, -1}, {-1, -1}, {-1, 0}}
	for _, direction := range directions {
		x, y := rMove+direction[0], cMove+direction[1]
		if x < 0 || x >= m || y < 0 || y >= n || board[x][y] == '.' || board[x][y] == color {
			continue
		}
		for x >= 0 && x < m && y >= 0 && y < n && board[x][y] != '.' {
			if board[x][y] == color {
				return true
			}
			x, y = x+direction[0], y+direction[1]
		}
	}
	return false
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
	var colorStr string
	if err := json.Unmarshal([]byte(inputValues[3]), &colorStr); err != nil {
		log.Fatal(err)
	}
	if len(colorStr) > 1 {
		color = colorStr[1]
	} else {
		color = colorStr[0]
	}

	return checkMove(board, rMove, cMove, color)
}
