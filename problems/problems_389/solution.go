package problem389

import (
	"encoding/json"
	"log"
	"strings"
)

func findTheDifference(s string, t string) byte {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var s string
	var t string

	if err := json.Unmarshal([]byte(values[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &t); err != nil {
		log.Fatal(err)
	}

	return findTheDifference(s, t)
}
