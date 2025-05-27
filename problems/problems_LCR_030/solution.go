package problemLCR_030

import (
	"encoding/json"
	"log"
	"strings"
)

type RandomizedSet struct {

}


/** Initialize your data structure here. */
func Constructor() RandomizedSet {

}


/** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
func (this *RandomizedSet) Insert(val int) bool {

}


/** Removes a value from the set. Returns true if the set contained the specified element. */
func (this *RandomizedSet) Remove(val int) bool {

}


/** Get a random element from the set. */
func (this *RandomizedSet) GetRandom() int {

}


/**
 * Your RandomizedSet object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Insert(val);
 * param_2 := obj.Remove(val);
 * param_3 := obj.GetRandom();
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
	obj := Constructor()
	ans = append(ans, nil)
	for i := 1; i < len(operators); i++ {
		var res any
		switch operators[i] {
		case "insert", "Insert":
			res = obj.Insert(int(opValues[i][0].(float64)))
		case "remove", "Remove":
			res = obj.Remove(int(opValues[i][0].(float64)))
		case "getRandom", "GetRandom":
			res = obj.GetRandom()
		default:
			res = nil
		}
		ans = append(ans, res)
	}


	return ans
}
