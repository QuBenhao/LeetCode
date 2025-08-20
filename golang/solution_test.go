package golang

import (
	problem "leetCode/problems/problems_652"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "652", "problems", problem.Solve)
}
