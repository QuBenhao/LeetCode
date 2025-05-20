package problem3001

import (
	"encoding/json"
	"log"
	"strings"
)

func minMovesToCaptureTheQueen(a int, b int, c int, d int, e int, f int) int {

}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var a int
	var b int
	var c int
	var d int
	var e int
	var f int

	if err := json.Unmarshal([]byte(inputValues[0]), &a); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &b); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &c); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &d); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[4]), &e); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[5]), &f); err != nil {
		log.Fatal(err)
	}

	return minMovesToCaptureTheQueen(a, b, c, d, e, f)
}
