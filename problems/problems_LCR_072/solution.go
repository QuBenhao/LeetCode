package problemLCR_072

import (
	"encoding/json"
	"log"
	"strings"
)

func mySqrt(x int) int {

}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var x int

	if err := json.Unmarshal([]byte(inputValues[0]), &x); err != nil {
		log.Fatal(err)
	}

	return mySqrt(x)
}
