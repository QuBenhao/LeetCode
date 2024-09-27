package problem2286

import (
	"encoding/json"
	"log"
	"strings"
)

type BookMyShow struct {

}


func Constructor(n int, m int) BookMyShow {

}


func (this *BookMyShow) Gather(k int, maxRow int) []int {

}


func (this *BookMyShow) Scatter(k int, maxRow int) bool {

}


/**
 * Your BookMyShow object will be instantiated and called as such:
 * obj := Constructor(n, m);
 * param_1 := obj.Gather(k,maxRow);
 * param_2 := obj.Scatter(k,maxRow);
 */

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var operators []string
	var opValues [][]interface{}
	var ans []interface{}
	if err := json.Unmarshal([]byte(inputValues[0]), &operators); err != nil {
		log.Println(err)
		return nil
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &opValues); err != nil {
		log.Println(err)
		return nil
	}
	obj := Constructor(int(opValues[0][0].(float64)), int(opValues[0][1].(float64)))
	ans = append(ans, nil)
	for i := 1; i < len(operators); i++ {
		var res interface{}
		switch operators[i] {
		case "gather", "Gather":
			res = obj.Gather(int(opValues[i][0].(float64)), int(opValues[i][1].(float64)))
		case "scatter", "Scatter":
			res = obj.Scatter(int(opValues[i][0].(float64)), int(opValues[i][1].(float64)))
		default:
			res = nil
		}
		ans = append(ans, res)
	}


	return ans
}
