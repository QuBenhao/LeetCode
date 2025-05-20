package problemLCR_018

import (
	"bytes"
	"encoding/json"
	"log"
	"strings"
)

func isPalindrome(s string) bool {
	isAlphaNumeric := func(c byte) bool {
		return (c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z') || (c >= '0' && c <= '9')
	}

	byteArr := []byte(s)
	byteArr = bytes.ToLower(byteArr)

	for left, right := 0, len(s)-1; left < right; left, right = left+1, right-1 {
		for left < right && !isAlphaNumeric(s[left]) {
			left++
		}
		for left < right && !isAlphaNumeric(s[right]) {
			right--
		}
		if byteArr[left] != byteArr[right] {
			return false
		}
	}
	return true
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return isPalindrome(s)
}
