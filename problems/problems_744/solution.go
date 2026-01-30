package problem744

import (
	"encoding/json"
	"log"
	"strings"
)

func nextGreatestLetter(letters []byte, target byte) byte {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var letters []byte
	var target byte

	var lettersStr []string
	if err := json.Unmarshal([]byte(inputValues[0]), &lettersStr); err != nil {
		log.Fatal(err)
	}
	letters = make([]byte, len(lettersStr))
	for i := 0; i < len(letters); i++ {
		letters[i] = lettersStr[i][0]
	}
	var targetStr string
	if err := json.Unmarshal([]byte(inputValues[1]), &targetStr); err != nil {
		log.Fatal(err)
	}
	if len(targetStr) > 1 {
		target = targetStr[1]
	} else {
		target = targetStr[0]
	}

	return nextGreatestLetter(letters, target)
}

func byteArrToStrArr(arr []byte) []string {
	ans := make([]string, len(arr))
	for i, b := range arr {
		ans[i] = string(b)
	}
	return ans
}
