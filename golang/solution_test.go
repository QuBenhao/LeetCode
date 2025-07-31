package golang

import (
	problem "leetCode/problems/problems_436"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "436", "problems", problem.Solve)
}
