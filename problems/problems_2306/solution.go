package problem2306

import (
	"encoding/json"
	"log"
	"strings"
)

func distinctNames(ideas []string) int64 {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var ideas []string

	if err := json.Unmarshal([]byte(inputValues[0]), &ideas); err != nil {
		log.Fatal(err)
	}

	return distinctNames(ideas)
}
