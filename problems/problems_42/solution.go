package problem42

import (
	"encoding/json"
	"log"
	"strings"
)

func trap(height []int) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var height []int

	if err := json.Unmarshal([]byte(inputValues[0]), &height); err != nil {
		log.Fatal(err)
	}

	return trap(height)
}
