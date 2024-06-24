package problem1056

import (
	"encoding/json"
	"log"
	"strings"
)

func confusingNumber(n int) bool {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var n int

	if err := json.Unmarshal([]byte(values[0]), &n); err != nil {
		log.Fatal(err)
	}

	return confusingNumber(n)
}
