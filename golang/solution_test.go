package golang

import (
	problem "leetCode/problems/problems_611"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "611", "problems", problem.Solve)
}
