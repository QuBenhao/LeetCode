package problem3200

import (
	"encoding/json"
	"log"
	"strings"
)

func maxHeightOfTriangle(red int, blue int) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var red int
	var blue int

	if err := json.Unmarshal([]byte(inputValues[0]), &red); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &blue); err != nil {
		log.Fatal(err)
	}

	return maxHeightOfTriangle(red, blue)
}
