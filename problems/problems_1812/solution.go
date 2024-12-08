package problem1812

import (
	"encoding/json"
	"log"
	"strings"
)

func squareIsWhite(coordinates string) bool {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var coordinates string

	if err := json.Unmarshal([]byte(inputValues[0]), &coordinates); err != nil {
		log.Fatal(err)
	}

	return squareIsWhite(coordinates)
}
