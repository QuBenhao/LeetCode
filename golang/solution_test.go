package golang

import (
	problem "leetCode/problems/problems_357"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "357", "problems", problem.Solve)
}
