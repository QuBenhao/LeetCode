package problem5

import (
	"encoding/json"
	"log"
	"strings"
)

func longestPalindrome(s string) string {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return longestPalindrome(s)
}
