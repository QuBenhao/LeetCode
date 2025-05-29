package problemLCR_071

import (
	"encoding/json"
	"log"
	"strings"
)

type Solution struct {

}


func Constructor(w []int) Solution {

}


func (this *Solution) PickIndex() int {

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
