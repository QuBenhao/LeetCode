package problem344

import (
	"encoding/json"
	"log"
	"strings"
)

func reverseString(s []byte) {
	for i, j := 0, len(s)-1; i < j; i++ {
		s[i], s[j] = s[j], s[i]
		j--
	}
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s []byte

	var sStr []string
	if err := json.Unmarshal([]byte(inputValues[0]), &sStr); err != nil {
		log.Fatal(err)
	}
	s = make([]byte, len(sStr))
	for i := 0; i < len(s); i++ {
		s[i] = sStr[i][0]
	}

	reverseString(s)
	return byteArrToStrArr(s)
}

func byteArrToStrArr(arr []byte) []string {
	ans := make([]string, len(arr))
	for i, b := range arr {
		ans[i] = string(b)
	}
	return ans
}
