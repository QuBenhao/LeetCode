package problem50

import (
	"encoding/json"
	"log"
	"strings"
)

func myPow(x float64, n int) float64 {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var x float64
	var n int

	if err := json.Unmarshal([]byte(values[0]), &x); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &n); err != nil {
		log.Fatal(err)
	}

	return myPow(x, n)
}
