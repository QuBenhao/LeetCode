package test

import (
	"encoding/json"
	"fmt"
	"github.com/stretchr/testify/assert"
	. "leetCode/golang/node_neighbours"
	"log"
	"testing"
)

func TestNodeNeighbour(t *testing.T) {
	var input [][]int
	if err := json.Unmarshal([]byte("[[2,4],[1,3],[2,4],[1,3]]"), &input); err != nil {
		log.Fatal(err)
	}
	node := ArrayRelationToNodeNeighbour(input)
	assert.Equal(t, 1, node.Val)
	assert.Len(t, node.Neighbors, 2)
	for _, nd := range node.Neighbors {
		assert.Contains(t, []int{2, 4}, nd.Val)
	}
	arr := NodeNeighbourToArrayRelation(node)
	assert.Equal(t, fmt.Sprintf("%v", input), fmt.Sprintf("%v", arr))
}
