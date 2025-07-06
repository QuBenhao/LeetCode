package problem1640

import (
	"encoding/json"
	"log"
	"strings"
)

func canFormArray(arr []int, pieces [][]int) bool {
	pieceMap := make(map[int][]int)
	for _, piece := range pieces {
		if len(piece) > 0 {
			pieceMap[piece[0]] = piece
		}
	}

	i := 0
	for i < len(arr) {
		if piece, found := pieceMap[arr[i]]; found {
			for _, num := range piece {
				if i < len(arr) && arr[i] == num {
					i++
				} else {
					return false
				}
			}
		} else {
			return false
		}
	}

	return true
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var arr []int
	var pieces [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &arr); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &pieces); err != nil {
		log.Fatal(err)
	}

	return canFormArray(arr, pieces)
}
