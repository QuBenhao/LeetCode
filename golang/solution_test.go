package golang

import (
	problem "leetCode/problems/problems_600"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "600", "problems", problem.Solve)
}
