package golang

import (
	problem "leetCode/problems/problems_219"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "219", "problems", problem.Solve)
}
