package problem419

import (
	"encoding/json"
	"log"
	"strings"
)

func countBattleships(board [][]byte) int {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var board [][]byte

	if err := json.Unmarshal([]byte(values[0]), &board); err != nil {
		log.Fatal(err)
	}

	return countBattleships(board)
}
