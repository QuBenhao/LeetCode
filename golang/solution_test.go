package golang

import (
	problem "leetCode/problems/problems_301"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "301", "problems", problem.Solve)
}
