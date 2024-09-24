package golang

import (
	"leetCode/problems/problems_LCR_083"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_083", "problems", problemLCR_083.Solve)
}
