package problem2710

import (
	"encoding/json"
	"log"
	"strings"
)

func removeTrailingZeros(num string) string {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var num string

	if err := json.Unmarshal([]byte(values[0]), &num); err != nil {
		log.Fatal(err)
	}

	return removeTrailingZeros(num)
}
