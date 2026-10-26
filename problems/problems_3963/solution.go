package problem3963

import (
	"encoding/json"
	"log"
	"strings"
)

func createGrid(m int, n int) []string {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var m int
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &m); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &n); err != nil {
		log.Fatal(err)
	}

	return createGrid(m, n)
}
