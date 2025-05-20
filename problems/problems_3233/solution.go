package problem3233

import (
	"encoding/json"
	"log"
	"strings"
)

func nonSpecialCount(l int, r int) int {

}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var l int
	var r int

	if err := json.Unmarshal([]byte(inputValues[0]), &l); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &r); err != nil {
		log.Fatal(err)
	}

	return nonSpecialCount(l, r)
}
