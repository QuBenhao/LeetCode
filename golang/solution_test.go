package golang

import (
	problem "leetCode/problems/problems_406"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "406", "problems", problem.Solve)
}
