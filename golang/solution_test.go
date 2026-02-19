package golang

import (
	problem "leetCode/problems/problems_761"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "761", "problems", problem.Solve)
}
