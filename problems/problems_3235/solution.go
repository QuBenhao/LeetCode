package problem3235

import (
	"encoding/json"
	"log"
	"strings"
)

func canReachCorner(xCorner int, yCorner int, circles [][]int) bool {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var xCorner int
	var yCorner int
	var circles [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &xCorner); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &yCorner); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &circles); err != nil {
		log.Fatal(err)
	}

	return canReachCorner(xCorner, yCorner, circles)
}
