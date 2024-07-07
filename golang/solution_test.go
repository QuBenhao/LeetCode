package golang

import (
	problem "leetCode/problems/problems_724"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "724", "problems", problem.Solve)
}
