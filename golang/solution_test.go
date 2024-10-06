package golang

import (
	problem "leetCode/problems/problems_871"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "871", "problems", problem.Solve)
}
