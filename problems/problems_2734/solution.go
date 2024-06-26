package problem2734

import (
	"encoding/json"
	"log"
	"strings"
)

func smallestString(s string) string {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var s string

	if err := json.Unmarshal([]byte(values[0]), &s); err != nil {
		log.Fatal(err)
	}

	return smallestString(s)
}
