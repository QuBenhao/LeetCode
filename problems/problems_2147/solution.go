package problem2147

import (
	"encoding/json"
	"log"
	"strings"
)

func numberOfWays(corridor string) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var corridor string

	if err := json.Unmarshal([]byte(inputValues[0]), &corridor); err != nil {
		log.Fatal(err)
	}

	return numberOfWays(corridor)
}
