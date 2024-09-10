package problemLCR_002

import (
	"encoding/json"
	"log"
	"slices"
	"strings"
)

func addBinary(a string, b string) string {
	var result []byte
	var carry int
	if len(a) < len(b) {
		a, b = b, a
	}
	for i, d := len(a)-1, len(a)-len(b); i >= 0; i-- {
		if a[i] == '1' {
			carry++
		}
		if i >= d && b[i-d] == '1' {
			carry++
		}
		result = append(result, byte(carry%2)+'0')
		carry /= 2
	}
	if carry > 0 {
		result = append(result, '1')
	}
	slices.Reverse(result)
	return string(result)
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var a string
	var b string

	if err := json.Unmarshal([]byte(inputValues[0]), &a); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &b); err != nil {
		log.Fatal(err)
	}

	return addBinary(a, b)
}
