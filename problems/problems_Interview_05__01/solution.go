package problemInterview_05__01

import (
	"encoding/json"
	"log"
	"strings"
)

func insertBits(N int, M int, i int, j int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var N int
	var M int
	var i int
	var j int

	if err := json.Unmarshal([]byte(inputValues[0]), &N); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &M); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &i); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &j); err != nil {
		log.Fatal(err)
	}

	return insertBits(N, M, i, j)
}
