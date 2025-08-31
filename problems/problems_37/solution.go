package problem37

import (
	"encoding/json"
	"log"
	"strings"
)

const N = 9

func solveSudoku(board [][]byte) {
	rows, cols, boxes := make([]int, N), make([]int, N), make([]int, N)
	for i := range N {
		for j := range N {
			if board[i][j] != '.' {
				v := 1 << (board[i][j] - '1')
				rows[i] |= v
				cols[j] |= v
				boxes[i/3*3+j/3] |= v
			}
		}
	}

	var backtrack func(i, j int) bool
	backtrack = func(i, j int) bool {
		if i == N {
			return true
		}
		if j == N {
			return backtrack(i+1, 0)
		}
		if board[i][j] != '.' {
			return backtrack(i, j+1)
		}
		for c := range N {
			v := 1 << c
			if rows[i]&v == 0 && cols[j]&v == 0 && boxes[i/3*3+j/3]&v == 0 {
				rows[i] |= v
				cols[j] |= v
				boxes[i/3*3+j/3] |= v
				board[i][j] = byte(c + '1')
				if backtrack(i, j+1) {
					return true
				}
				rows[i] &^= v
				cols[j] &^= v
				boxes[i/3*3+j/3] &^= v
				board[i][j] = '.'
			}
		}
		return false
	}
	backtrack(0, 0)
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

	solveSudoku(board)
	return byteArrToStrArr(board)
}

func byteArrToStrArr(arr [][]byte) [][]string {
	ans := make([][]string, len(arr))
	for i, b := range arr {
		ans[i] = make([]string, len(b))
		for j, v := range b {
			ans[i][j] = string(v)
		}
	}
	return ans
}
