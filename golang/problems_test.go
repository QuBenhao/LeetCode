package golang

import (
	"leetCode/problems/problems_LCR_032"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_032", "problems", problemLCR_032.Solve)
}
