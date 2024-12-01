package golang

import (
	problem "leetCode/problems/problems_52"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "52", "problems", problem.Solve)
}
