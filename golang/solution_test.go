package golang

import (
	problem "leetCode/problems/problems_541"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "541", "problems", problem.Solve)
}
