package golang

import (
	problem "leetCode/problems/problems_835"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "835", "problems", problem.Solve)
}
