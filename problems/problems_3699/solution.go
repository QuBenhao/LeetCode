package problem3699

import (
	"encoding/json"
	"log"
	"strings"
)

func zigZagArrays(n int, l int, r int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var l int
	var r int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &l); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &r); err != nil {
		log.Fatal(err)
	}

	return zigZagArrays(n, l, r)
}
