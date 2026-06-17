package problem1344

import (
	"encoding/json"
	"log"
	"strings"
)

func angleClock(hour int, minutes int) float64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var hour int
	var minutes int

	if err := json.Unmarshal([]byte(inputValues[0]), &hour); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &minutes); err != nil {
		log.Fatal(err)
	}

	return angleClock(hour, minutes)
}
