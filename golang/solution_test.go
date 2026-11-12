package golang

import (
	problem "leetCode/problems/problems_3420"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "3420", "problems", problem.Solve)
}
