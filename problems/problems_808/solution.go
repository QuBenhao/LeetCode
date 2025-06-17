package problem808

import (
	"encoding/json"
	"log"
	"strings"
)

func soupServings(n int) float64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return soupServings(n)
}
