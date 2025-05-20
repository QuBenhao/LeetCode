package problem51

import (
	"encoding/json"
	"log"
	"strings"
)

func solveNQueens(n int) (ans [][]string) {
	var ansQueens [][]int
	var backtrack func(row int, columns, diagonals, antiDiagonals []bool, queens []int)
	backtrack = func(row int, columns, diagonals, antiDiagonals []bool, queens []int) {
		if row == n {
			ansQueens = append(ansQueens, append([]int{}, queens...))
			return
		}
		for col := 0; col < n; col++ {
			idx1 := col + row
			idx2 := n - 1 - row + col
			if columns[col] || diagonals[idx1] || antiDiagonals[idx2] {
				continue
			}
			columns[col], diagonals[idx1], antiDiagonals[idx2] = true, true, true
			queens = append(queens, col)
			backtrack(row+1, columns, diagonals, antiDiagonals, queens)
			queens = queens[:len(queens)-1]
			columns[col], diagonals[idx1], antiDiagonals[idx2] = false, false, false
		}
	}
	columns := make([]bool, n)
	diagonals := make([]bool, 2*n)
	antiDiagonals := make([]bool, 2*n)
	for i := range columns {
		columns[i] = false
	}
	for i := range diagonals {
		diagonals[i] = false
		antiDiagonals[i] = false
	}
	backtrack(0, columns, diagonals, antiDiagonals, []int{})
	for _, queens := range ansQueens {
		var board []string
		for _, col := range queens {
			row := strings.Repeat(".", col) + "Q" + strings.Repeat(".", n-1-col)
			board = append(board, row)
		}
		ans = append(ans, board)
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return solveNQueens(n)
}
