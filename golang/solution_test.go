package golang

import (
	problem "leetCode/problems/problems_735"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "735", "problems", problem.Solve)
}
