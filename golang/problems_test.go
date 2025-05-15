package golang

import (
	"leetCode/problems/problems_LCR_102"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_102", "problems", problemLCR_102.Solve)
}
