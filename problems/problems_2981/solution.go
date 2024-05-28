package problem2981

import (
	"encoding/json"
	"log"
	"strings"
)

func maximumLength(s string) int {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var s string

	if err := json.Unmarshal([]byte(values[0]), &s); err != nil {
		log.Fatal(err)
	}

	return maximumLength(s)
}
