package problem838

import (
	"encoding/json"
	"log"
	"strings"
)

func pushDominoes(dominoes string) string {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var dominoes string

	if err := json.Unmarshal([]byte(inputValues[0]), &dominoes); err != nil {
		log.Fatal(err)
	}

	return pushDominoes(dominoes)
}
