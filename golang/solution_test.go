package golang

import (
	problem "leetCode/problems/problems_32"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "32", "problems", problem.Solve)
}
