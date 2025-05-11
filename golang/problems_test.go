package golang

import (
	"leetCode/problems/problems_LCR_040"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_040", "problems", problemLCR_040.Solve)
}
