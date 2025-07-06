package problem3602

import (
	"bytes"
	"encoding/json"
	"log"
	"slices"
	"strings"
)

const hex36 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

func concatHex36(n int) string {
	x := n * n
	y := x * n
	var buf bytes.Buffer
	for y > 0 {
		buf.WriteByte(hex36[y%36])
		y /= 36
	}
	for x > 0 {
		buf.WriteByte(hex36[x%16])
		x /= 16
	}
	// reverse the buffer to get the correct order
	slices.Reverse(buf.Bytes())
	return buf.String()
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return concatHex36(n)
}
