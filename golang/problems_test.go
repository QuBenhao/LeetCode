package golang

import (
	"leetCode/problems/problems_17"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "17", "problems", problem17.Solve)
}
