package golang

import (
	"leetCode/problems/problems_LCR_012"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_012", "problems", problemLCR_012.Solve)
}
