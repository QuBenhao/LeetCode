package problemInterview_01__01

import (
	"encoding/json"
	"log"
	"strings"
)

func isUnique(astr string) bool {
	var mark int32
	for _, v := range astr {
		if cur := int32(1) << (v - 'a'); mark&cur != 0 {
			return false
		} else {
			mark |= cur
		}
	}
	return true
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var astr string

	if err := json.Unmarshal([]byte(inputValues[0]), &astr); err != nil {
		log.Fatal(err)
	}

	return isUnique(astr)
}
