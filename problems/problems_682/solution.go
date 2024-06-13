package problem682

import (
	"encoding/json"
	"log"
	"strings"
)

func calPoints(operations []string) int {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var operations []string

	if err := json.Unmarshal([]byte(values[0]), &operations); err != nil {
		log.Fatal(err)
	}

	return calPoints(operations)
}
