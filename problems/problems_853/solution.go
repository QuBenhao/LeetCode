package problem853

import (
	"encoding/json"
	"log"
	"strings"
)

func carFleet(target int, position []int, speed []int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var target int
	var position []int
	var speed []int

	if err := json.Unmarshal([]byte(inputValues[0]), &target); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &position); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &speed); err != nil {
		log.Fatal(err)
	}

	return carFleet(target, position, speed)
}
