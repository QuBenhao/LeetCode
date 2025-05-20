package problem2338

import (
	"encoding/json"
	"log"
	"strings"
)

func idealArrays(n int, maxValue int) int {

}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var maxValue int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &maxValue); err != nil {
		log.Fatal(err)
	}

	return idealArrays(n, maxValue)
}
