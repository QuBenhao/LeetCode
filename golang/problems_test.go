package golang

import (
	"leetCode/problems/problems_72"
	"leetCode/problems/problems_LCR_037"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_037", "problems", problemLCR_037.Solve)
	TestEach(t, "72", "problems", problem72.Solve)
}
