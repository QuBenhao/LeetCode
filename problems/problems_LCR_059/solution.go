package problemLCR_059

import (
	"encoding/json"
	"log"
	"strings"
)

type KthLargest struct {

}


func Constructor(k int, nums []int) KthLargest {

}


func (this *KthLargest) Add(val int) int {

}


/**
 * Your KthLargest object will be instantiated and called as such:
 * obj := Constructor(k, nums);
 * param_1 := obj.Add(val);
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
	obj := Constructor(int(opValues[0][0].(float64)), opValues[0][1].([]int))
	ans = append(ans, nil)
	for i := 1; i < len(operators); i++ {
		var res interface{}
		switch operators[i] {
		case "add", "Add":
			res = obj.Add(int(opValues[i][0].(float64)))
		default:
			res = nil
		}
		ans = append(ans, res)
	}


	return ans
}
