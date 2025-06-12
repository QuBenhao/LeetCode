package problem133

import (
	"encoding/json"
	. "leetCode/golang/node_neighbours"
	"log"
	"strings"
)

/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Neighbors []*Node
 * }
 */

func cloneGraph(node *Node) *Node {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var node *Node

	var arr0 [][]int
	if err := json.Unmarshal([]byte(inputValues[0]), &arr0); err != nil {
		log.Fatal(err)
	}
	node = ArrayRelationToNodeNeighbour(arr0)

	return NodeNeighbourToArrayRelation(cloneGraph(node))
}
