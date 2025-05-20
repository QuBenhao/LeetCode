package problem1472

import (
	"encoding/json"
	"log"
	"strings"
)

type BrowserHistory struct {
	back    []string
	forward []string
}

func Constructor(homepage string) BrowserHistory {
	return BrowserHistory{
		back: []string{homepage},
	}
}

func (this *BrowserHistory) Visit(url string) {
	this.back = append(this.back, url)
	for len(this.forward) > 0 {
		this.forward = this.forward[:len(this.forward)-1]
	}
}

func (this *BrowserHistory) Back(steps int) string {
	n := len(this.back) - 1
	for i := 0; i < steps && i < n; i++ {
		elem := this.back[len(this.back)-1]
		this.back = this.back[:len(this.back)-1]
		this.forward = append(this.forward, elem)
	}
	return this.back[len(this.back)-1]
}

func (this *BrowserHistory) Forward(steps int) string {
	n := len(this.forward)
	for i := 0; i < steps && i < n; i++ {
		elem := this.forward[len(this.forward)-1]
		this.forward = this.forward[:len(this.forward)-1]
		this.back = append(this.back, elem)
	}
	return this.back[len(this.back)-1]
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * obj := Constructor(homepage);
 * obj.Visit(url);
 * param_2 := obj.Back(steps);
 * param_3 := obj.Forward(steps);
 */

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var opts []string
	var vals [][]any
	var ans []any
	if err := json.Unmarshal([]byte(values[0]), &opts); err != nil {
		log.Println(err)
		return nil
	}
	if err := json.Unmarshal([]byte(values[1]), &vals); err != nil {
		log.Println(err)
		return nil
	}
	obj := Constructor(vals[0][0].(string))
	ans = append(ans, nil)
	for i := 1; i < len(opts); i++ {
		var res any
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
