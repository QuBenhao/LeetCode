package problem1812

import (
	"encoding/json"
	"log"
	"strings"
)

func squareIsWhite(coordinates string) bool {
	return (int(coordinates[0]-'a')+int(coordinates[1]-'1'))%2 == 1
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var coordinates string

	if err := json.Unmarshal([]byte(inputValues[0]), &coordinates); err != nil {
		log.Fatal(err)
	}

	return squareIsWhite(coordinates)
}
