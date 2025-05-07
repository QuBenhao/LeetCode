package golang

import (
	"leetCode/problems/problems_LCR_101"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_101", "problems", problemLCR_101.Solve)
}
