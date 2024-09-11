package golang

import (
	"leetCode/problems/problems_LCR_043"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_043", "problems", problemLCR_043.Solve)
}
