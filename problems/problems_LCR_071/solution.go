package problemLCR_071

import (
	"encoding/json"
	"log"
	"math/rand"
	"strings"
)

type Solution struct {
	Prefix []int
}

func Constructor(w []int) Solution {
	n := len(w)
	prefix := make([]int, n+1)
	for i, v := range w {
		prefix[i+1] = prefix[i] + v
	}
	return Solution{prefix}
}

func (sol *Solution) PickIndex() int {
	v := rand.Intn(sol.Prefix[len(sol.Prefix)-1]) + 1
	left, right := 1, len(sol.Prefix)-1
	for left < right {
		mid := ((right - left) >> 1) + left
		if sol.Prefix[mid] < v {
			left = mid + 1
		} else {
			right = mid
		}
	}
	return left - 1
}

/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(w);
 * param_1 := obj.PickIndex();
 */

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var operators []string
	var opValues [][]any
	var ans []any
	if err := json.Unmarshal([]byte(inputValues[0]), &operators); err != nil {
		log.Println(err)
		return nil
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &opValues); err != nil {
		log.Println(err)
		return nil
	}
	var wArr []int
	if v, ok := opValues[0][0].([]int); ok {
		wArr = v
	} else {
		for _, vi := range opValues[0][0].([]any) {
			wArr = append(wArr, int(vi.(float64)))
		}
	}
	obj := Constructor(wArr)
	ans = append(ans, nil)
	for i := 1; i < len(operators); i++ {
		var res any
		switch operators[i] {
		case "pickIndex", "PickIndex":
			res = obj.PickIndex()
		default:
			res = nil
		}
		ans = append(ans, res)
	}

	return ans
}
