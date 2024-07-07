package golang

import (
	"leetCode/problems/problems_70"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "70", "problems", problem70.Solve)
}
