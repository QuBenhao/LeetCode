package golang

import (
	problem "leetCode/problems/problems_407"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "407", "problems", problem.Solve)
}
