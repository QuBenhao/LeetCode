package golang

import (
	"leetCode/problems/problems_LCR_119"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_119", "problems", problemLCR_119.Solve)
}
