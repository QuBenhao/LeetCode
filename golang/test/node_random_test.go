package test

import (
	"encoding/json"
	"fmt"
	"github.com/stretchr/testify/assert"
	"leetCode/golang/list_random"
	"log"
	"testing"
)

func TestRandomNode(t *testing.T) {
	var input [][]interface{}
	if err := json.Unmarshal([]byte("[[7,null],[13,0],[11,4],[10,2],[1,0]]"), &input); err != nil {
		log.Fatal(err)
	}
	head := list_random.IntRandomArrayToNodeArray(input)
	assert.NotNil(t, head)
	assert.Equal(t, 7, head.Val)
	assert.Nil(t, head.Random)
	assert.Equal(t, head, head.Next.Random)
	res := list_random.NodeArrayToIntRandomArray(head)
	assert.Equal(t, fmt.Sprintf("%v", input), fmt.Sprintf("%v", res))
}
