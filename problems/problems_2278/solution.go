package problem2278

import (
	"encoding/json"
	"log"
	"strings"
)

func percentageLetter(s string, letter byte) (ans int) {
	for b := range s {
		if s[b] == letter {
			ans++
		}
	}
	return ans * 100 / len(s)
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string
	var letter byte

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}
	var letterStr string
	if err := json.Unmarshal([]byte(inputValues[1]), &letterStr); err != nil {
		log.Fatal(err)
	}
	if len(letterStr) > 1 {
		letter = letterStr[1]
	} else {
		letter = letterStr[0]
	}

	return percentageLetter(s, letter)
}
