package golang

import (
	problem "leetCode/problems/problems_743"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "743", "problems", problem.Solve)
}
