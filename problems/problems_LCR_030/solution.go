package problemLCR_030

import (
	"encoding/json"
	"log"
	"math/rand/v2"
	"strings"
)

type RandomizedSet struct {
	vals   []int
	valMap map[int]int
}

/** Initialize your data structure here. */
func Constructor() RandomizedSet {
	return RandomizedSet{
		vals:   []int{},
		valMap: make(map[int]int),
	}
}

/** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
func (rs *RandomizedSet) Insert(val int) bool {
	if _, exists := rs.valMap[val]; exists {
		return false // Value already exists in the set
	}
	rs.vals = append(rs.vals, val)
	rs.valMap[val] = len(rs.vals) - 1 // Store the index of the value
	return true
}

/** Removes a value from the set. Returns true if the set contained the specified element. */
func (rs *RandomizedSet) Remove(val int) bool {
	if _, exists := rs.valMap[val]; !exists {
		return false
	}
	index := rs.valMap[val]
	n := len(rs.vals) - 1
	rs.vals[index], rs.vals[n] = rs.vals[n], rs.vals[index] // Swap with the last element
	rs.valMap[rs.vals[index]] = index                       // Update the index of the swapped element
	delete(rs.valMap, val)                                  // Remove the value from the map
	rs.vals = rs.vals[:n]                                   // Remove the last element
	return true
}

/** Get a random element from the set. */
func (rs *RandomizedSet) GetRandom() int {
	return rs.vals[rand.IntN(len(rs.vals))]
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
