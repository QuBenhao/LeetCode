package golang

import (
	problem "leetCode/problems/problems_784"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "784", "problems", problem.Solve)
}
