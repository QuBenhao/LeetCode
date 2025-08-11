package problem2787

import (
	"encoding/json"
	"log"
	"strings"
)

func numberOfWays(n int, x int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var x int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &x); err != nil {
		log.Fatal(err)
	}

	return numberOfWays(n, x)
}
