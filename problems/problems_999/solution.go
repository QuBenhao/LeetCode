package problem999

import (
	"encoding/json"
	"log"
	"strings"
)

func numRookCaptures(board [][]byte) (ans int) {
	directions := [][]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
	m, n := len(board), len(board[0])
	var x, y int
	x = -1
	for i, row := range board {
		for j, v := range row {
			if v == 'R' {
				x = i
				y = j
				break
			}
		}
		if x != -1 {
			break
		}
	}
	for _, d := range directions {
		curX, curY := x, y
		for true {
			nxtX, nxtY := curX+d[0], curY+d[1]
			if nxtX < 0 || nxtX == m || nxtY < 0 || nxtY == n {
				break
			}
			if board[nxtX][nxtY] == 'B' {
				break
			} else if board[nxtX][nxtY] == 'p' {
				ans++
				break
			}
			curX, curY = nxtX, nxtY
		}
	}
	return
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
