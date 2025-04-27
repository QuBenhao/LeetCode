package golang

import (
	"leetCode/problems/problems_LCR_116"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_116", "problems", problemLCR_116.Solve)
}
