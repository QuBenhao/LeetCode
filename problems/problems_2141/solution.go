package problem2141

import (
	"encoding/json"
	"log"
	"strings"
)

func maxRunTime(n int, batteries []int) int64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var batteries []int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &batteries); err != nil {
		log.Fatal(err)
	}

	return maxRunTime(n, batteries)
}
