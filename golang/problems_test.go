package golang

import (
	"leetCode/problems/problems_LCR_025"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_025", "problems", problemLCR_025.Solve)
}
