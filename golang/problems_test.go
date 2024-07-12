package golang

import (
	"leetCode/problems/problems_206"
	"leetCode/problems/problems_74"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "206", "problems", problem206.Solve)
	TestEach(t, "74", "problems", problem74.Solve)
}
