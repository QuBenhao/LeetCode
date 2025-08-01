package golang

import (
	problem "leetCode/problems/problems_691"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "691", "problems", problem.Solve)
}
