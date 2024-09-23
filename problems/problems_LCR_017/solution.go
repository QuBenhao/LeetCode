package problemLCR_017

import (
	"encoding/json"
	"log"
	"strings"
)

func minWindow(s string, t string) string {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string
	var t string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &t); err != nil {
		log.Fatal(err)
	}

	return minWindow(s, t)
}
