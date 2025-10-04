package golang

import (
	problem "leetCode/problems/problems_417"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "417", "problems", problem.Solve)
}
