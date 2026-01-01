package golang

import (
	problem "leetCode/problems/problems_961"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "961", "problems", problem.Solve)
}
