package golang

import (
	problem "leetCode/problems/problems_48"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "48", "problems", problem.Solve)
}
