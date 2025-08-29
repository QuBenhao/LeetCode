package problem3021

import (
	"encoding/json"
	"log"
	"strings"
)

func flowerGame(n int, m int) int64 {
	return int64(n/2)*int64((m+1)/2) + int64((n+1)/2)*int64(m/2)
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var m int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &m); err != nil {
		log.Fatal(err)
	}

	return flowerGame(n, m)
}
