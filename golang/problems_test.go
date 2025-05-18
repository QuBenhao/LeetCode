package golang

import (
	"leetCode/problems/problems_LCR_020"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_020", "problems", problemLCR_020.Solve)
}
