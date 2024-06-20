package problem1472

import (
	"encoding/json"
	"log"
	"strings"
)

type BrowserHistory struct {

}


func Constructor(homepage string) BrowserHistory {

}


func (this *BrowserHistory) Visit(url string)  {

}


func (this *BrowserHistory) Back(steps int) string {

}


func (this *BrowserHistory) Forward(steps int) string {

}


/**
 * Your BrowserHistory object will be instantiated and called as such:
 * obj := Constructor(homepage);
 * obj.Visit(url);
 * param_2 := obj.Back(steps);
 * param_3 := obj.Forward(steps);
 */

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var opts []string
	var vals [][]interface{}
	var ans []interface{}
	if err := json.Unmarshal([]byte(values[0]), &opts); err != nil {
		log.Println(err)
		return nil
	}
	if err := json.Unmarshal([]byte(values[1]), &vals); err != nil {
		log.Println(err)
		return nil
	}
	obj :=Constructor(vals[0][0].(string))
	ans = append(ans, nil)
	for i := 1; i < len(opts); i++ {
		var res interface{}
		switch opts[i] {
		case "visit", "Visit":
			res = nil
			obj.Visit(vals[i][0].(string))
		case "back", "Back":
			res = obj.Back(int(vals[i][0].(float64)))
		case "forward", "Forward":
			res = obj.Forward(int(vals[i][0].(float64)))
		default:
			res = nil
		}
		ans = append(ans, res)
	}


	return ans
}
