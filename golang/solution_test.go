package golang

import (
	problem "leetCode/problems/problems_732"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "732", "problems", problem.Solve)
}
