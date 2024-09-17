package golang

import (
	"leetCode/problems/problems_LCR_108"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_108", "problems", problemLCR_108.Solve)
}
