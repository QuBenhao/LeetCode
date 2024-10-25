package golang

import (
	"leetCode/problems/problems_LCR_111"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_111", "problems", problemLCR_111.Solve)
}
