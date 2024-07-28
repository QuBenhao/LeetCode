package golang

import (
	problem "leetCode/problems/problems_682"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "682", "problems", problem.Solve)
}
