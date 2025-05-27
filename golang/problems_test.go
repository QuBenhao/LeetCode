package golang

import (
	"leetCode/problems/problems_LCR_030"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_030", "problems", problemLCR_030.Solve)
}
