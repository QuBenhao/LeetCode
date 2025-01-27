package golang

import (
	problem "leetCode/problems/problems_119"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "119", "problems", problem.Solve)
}
