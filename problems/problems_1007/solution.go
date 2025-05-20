package problem1007

import (
	"encoding/json"
	"log"
	"math"
	"strings"
)

func minDominoRotations(tops []int, bottoms []int) int {
	n, ans1, ans2, ans3, ans4 := len(tops), 0, 0, 0, 0
	tp, bt := tops[0], bottoms[0]
	for i := 0; i < n; i++ {
		t, b := tops[i], bottoms[i]
		if t != tp && b != tp {
			ans1 = -1
			ans3 = -1
		} else {
			if t != tp && ans1 != -1 {
				ans1++
			}
			if b != tp && ans3 != -1 {
				ans3++
			}
		}
		if t != bt && b != bt {
			ans2 = -1
			ans4 = -1
		} else {
			if t != bt && ans2 != -1 {
				ans2++
			}
			if b != bt && ans4 != -1 {
				ans4++
			}
		}
		if ans1 == -1 && ans2 == -1 && ans3 == -1 && ans4 == -1 {
			return -1
		}
	}
	convert := func(x int) int {
		if x == -1 {
			return math.MaxInt
		}
		return x
	}
	return min(convert(ans1), convert(ans2), convert(ans3), convert(ans4))
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var tops []int
	var bottoms []int

	if err := json.Unmarshal([]byte(inputValues[0]), &tops); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &bottoms); err != nil {
		log.Fatal(err)
	}

	return minDominoRotations(tops, bottoms)
}
