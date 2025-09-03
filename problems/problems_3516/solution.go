package problem3516

import (
	"encoding/json"
	"log"
	"strings"
)

func findClosest(x int, y int, z int) int {
	d1, d2 := abs(x-z), abs(y-z)
	if d := d1 - d2; d == 0 {
		return 0
	} else if d < 0 {
		return 1
	} else {
		return 2
	}
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var x int
	var y int
	var z int

	if err := json.Unmarshal([]byte(inputValues[0]), &x); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &y); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &z); err != nil {
		log.Fatal(err)
	}

	return findClosest(x, y, z)
}
