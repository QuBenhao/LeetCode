package problem2402

import (
	"encoding/json"
	"log"
	"strings"
)

func mostBooked(n int, meetings [][]int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var meetings [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &meetings); err != nil {
		log.Fatal(err)
	}

	return mostBooked(n, meetings)
}
