package golang

import (
	problem "leetCode/problems/problems_135"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "135", "problems", problem.Solve)
}
