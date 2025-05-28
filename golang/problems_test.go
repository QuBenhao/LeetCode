package golang

import (
	"leetCode/problems/problems_LCR_041"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_041", "problems", problemLCR_041.Solve)
}
