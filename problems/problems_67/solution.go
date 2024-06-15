package problem67

import (
	"encoding/json"
	"log"
	"strings"
)

func addBinary(a string, b string) string {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var a string
	var b string

	if err := json.Unmarshal([]byte(values[0]), &a); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &b); err != nil {
		log.Fatal(err)
	}

	return addBinary(a, b)
}
