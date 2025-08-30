package problem36

import (
	"encoding/json"
	"log"
	"strings"
)

const N = 9

func isValidSudoku(board [][]byte) bool {
	for i := range N {
		r, c, b := 0, 0, 0
		for j := range N {
			if board[i][j] != '.' {
				v := 1 << (board[i][j] - '1')
				if r&v != 0 {
					return false
				}
				r |= v
			}
			if board[j][i] != '.' {
				v := 1 << (board[j][i] - '1')
				if c&v != 0 {
					return false
				}
				c |= v
			}
			bi := (i/3)*3 + j/3
			bj := (i%3)*3 + j%3
			if board[bi][bj] != '.' {
				v := 1 << (board[bi][bj] - '1')
				if b&v != 0 {
					return false
				}
				b |= v
			}
		}
	}
	return true
}

func Solve(inputJsonValues string) any {
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

	return isValidSudoku(board)
}

func byteArrToStrArr(arr [][]byte) []string {
	ans := make([]string, len(arr))
	for i, b := range arr {
		ans[i] = string(b)
	}
	return ans
}
