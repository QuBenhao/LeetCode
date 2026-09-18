package problem1401

import (
	"encoding/json"
	"log"
	"strings"
)

func checkOverlap(radius int, xCenter int, yCenter int, x1 int, y1 int, x2 int, y2 int) bool {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var radius int
	var xCenter int
	var yCenter int
	var x1 int
	var y1 int
	var x2 int
	var y2 int

	if err := json.Unmarshal([]byte(inputValues[0]), &radius); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &xCenter); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &yCenter); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &x1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[4]), &y1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[5]), &x2); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[6]), &y2); err != nil {
		log.Fatal(err)
	}

	return checkOverlap(radius, xCenter, yCenter, x1, y1, x2, y2)
}
