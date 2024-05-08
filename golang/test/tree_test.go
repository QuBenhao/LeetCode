package test

import (
	"github.com/stretchr/testify/assert"
	. "leetCode/golang/models"
	"testing"
)

func TestTree(t *testing.T) {
	node := ArrayToTree("[1,null,2]")
	assert.NotNil(t, node)
	assert.Equal(t, 1, node.Val)
	assert.Nil(t, node.Left)
	assert.Equal(t, 2, node.Right.Val)
}
