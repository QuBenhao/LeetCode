package golang

import (
	problem "leetCode/problems/problems_976"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "976", "problems", problem.Solve)
}
