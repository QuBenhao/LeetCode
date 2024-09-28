package problemLCR_071

import (

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
	var arr []int
	if v, ok := opValues[0][0].([]int); ok {
		arr = v
	} else {
		for _, vi := range opValues[0][0].([]interface{}) {
			arr = append(arr, int(vi.(float64)))
		}
	}
	obj := Constructor(arr)
	ans = append(ans, nil)
	for i := 1; i < len(operators); i++ {
		var res interface{}
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
