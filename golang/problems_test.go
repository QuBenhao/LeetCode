package golang

import (
	"leetCode/problems/problems_279"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "279", "problems", problem279.Solve)
}
