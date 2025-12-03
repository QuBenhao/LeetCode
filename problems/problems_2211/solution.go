package problem2211

import (
	"encoding/json"
	"log"
	"strings"
)

func countCollisions(directions string) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var directions string

	if err := json.Unmarshal([]byte(inputValues[0]), &directions); err != nil {
		log.Fatal(err)
	}

	return countCollisions(directions)
}
