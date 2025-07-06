package problem3609

import (
	"encoding/json"
	"log"
	"strings"
)

func minMoves(sx int, sy int, tx int, ty int) (ans int) {
	if sx == tx && sy == ty {
		return 0
	}
	if sx > tx || sy > ty {
		return -1
	}
	if tx == ty {
		if sx == 0 {
			sx, sy, tx, ty = sy, sx, ty, tx
		}
		ans = minMoves(sx, sy, tx, 0)
	} else {
		if tx < ty {
			sx, sy, tx, ty = sy, sx, ty, tx
		}
		if tx > ty*2 {
			if tx&1 == 1 {
				return -1
			}
			ans = minMoves(sx, sy, tx/2, ty)
		} else {
			ans = minMoves(sx, sy, tx-ty, ty)
		}
	}
	if ans != -1 {
		ans++
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var sx int
	var sy int
	var tx int
	var ty int

	if err := json.Unmarshal([]byte(inputValues[0]), &sx); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &sy); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &tx); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &ty); err != nil {
		log.Fatal(err)
	}

	return minMoves(sx, sy, tx, ty)
}
