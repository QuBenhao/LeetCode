package golang

import (
	problem "leetCode/problems/problems_209"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "209", "problems", problem.Solve)
}
