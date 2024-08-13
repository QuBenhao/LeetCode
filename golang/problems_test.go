package golang

import (
	"leetCode/problems/problems_199"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "199", "problems", problem199.Solve)
}
