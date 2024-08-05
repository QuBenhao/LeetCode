package problem438

import (
	"encoding/json"
	"log"
	"strings"
)

func findAnagrams(s string, p string) []int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string
	var p string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &p); err != nil {
		log.Fatal(err)
	}

	return findAnagrams(s, p)
}
