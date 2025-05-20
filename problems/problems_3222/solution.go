package problem3222

import (
	"encoding/json"
	"log"
	"strings"
)

func losingPlayer(x int, y int) string {

}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var x int
	var y int

	if err := json.Unmarshal([]byte(inputValues[0]), &x); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &y); err != nil {
		log.Fatal(err)
	}

	return losingPlayer(x, y)
}
