package problem2663

import (
	"encoding/json"
	"log"
	"strings"
)

func smallestBeautifulString(s string, k int) string {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var s string
	var k int

	if err := json.Unmarshal([]byte(values[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &k); err != nil {
		log.Fatal(err)
	}

	return smallestBeautifulString(s, k)
}
