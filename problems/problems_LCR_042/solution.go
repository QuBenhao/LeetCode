package problemLCR_042

import (
	"encoding/json"
	"log"
	"strings"
)

type RecentCounter struct {

}


func Constructor() RecentCounter {

}


func (this *RecentCounter) Ping(t int) int {

}


/**
 * Your RecentCounter object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Ping(t);
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
	obj := Constructor()
	ans = append(ans, nil)
	for i := 1; i < len(operators); i++ {
		var res interface{}
		switch operators[i] {
		case "ping", "Ping":
			res = obj.Ping(int(opValues[i][0].(float64)))
		default:
			res = nil
		}
		ans = append(ans, res)
	}


	return ans
}
