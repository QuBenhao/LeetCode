package problem36

import (
	"encoding/json"
	"log"
	"strings"
)

func isValidSudoku(board [][]byte) bool {
    
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
