package problem756

import (
	"encoding/json"
	"log"
	"strings"
)

func pyramidTransition(bottom string, allowed []string) bool {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var bottom string
	var allowed []string

	if err := json.Unmarshal([]byte(inputValues[0]), &bottom); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &allowed); err != nil {
		log.Fatal(err)
	}

	return pyramidTransition(bottom, allowed)
}
