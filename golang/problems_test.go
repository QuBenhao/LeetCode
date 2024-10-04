package golang

import (
	"leetCode/problems/problems_LCR_052"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_052", "problems", problemLCR_052.Solve)
}
