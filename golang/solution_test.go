package golang

import (
	problem "leetCode/problems/problems_904"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "904", "problems", problem.Solve)
}
