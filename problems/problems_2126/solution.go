package problem2126

import (
	"encoding/json"
	"log"
	"strings"
)

func asteroidsDestroyed(mass int, asteroids []int) bool {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var mass int
	var asteroids []int

	if err := json.Unmarshal([]byte(inputValues[0]), &mass); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &asteroids); err != nil {
		log.Fatal(err)
	}

	return asteroidsDestroyed(mass, asteroids)
}
