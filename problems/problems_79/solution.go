package problem79

import (
	"encoding/json"
	"log"
	"strings"
)

func exist(board [][]byte, word string) bool {
	dirs := [][]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}
	m, n := len(board), len(board[0])
	sl := len(word)

	var backtrack func(int, int, int) bool
	backtrack = func(i, j, k int) bool {
		if i < 0 || i >= m || j < 0 || j >= n || board[i][j] != word[k] {
			return false
		}
		if k == sl-1 {
			return true
		}
		tmp := board[i][j]
		board[i][j] = ' '
		for _, dir := range dirs {
			if backtrack(i+dir[0], j+dir[1], k+1) {
				return true
			}
		}
		board[i][j] = tmp
		return false
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if backtrack(i, j, 0) {
				return true
			}
		}
	}
	return false
}

func Solve(inputJsonValues string) any {
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
