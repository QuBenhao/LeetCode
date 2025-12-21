package problemInterview_16__04

import (
	"encoding/json"
	"log"
	"strings"
)

func tictactoe(board []string) string {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var board []string

	if err := json.Unmarshal([]byte(inputValues[0]), &board); err != nil {
		log.Fatal(err)
	}

	return tictactoe(board)
}
