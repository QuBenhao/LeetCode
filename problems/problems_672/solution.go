package problem672

import (
	"encoding/json"
	"log"
	"strings"
)

func flipLights(n int, presses int) int {
	if presses == 0 {
		return 1
	}
	if n == 1 {
		return 2
	}
	if n == 2 {
		if presses == 1 {
			return 3
		}
		return 4
	}
	if presses == 1 {
		return 4
	}
	if presses == 2 {
		return 7
	}
	return 8
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var presses int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &presses); err != nil {
		log.Fatal(err)
	}

	return flipLights(n, presses)
}
