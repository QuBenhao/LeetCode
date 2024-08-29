package golang

import (
	"leetCode/problems/problems_148"
	"leetCode/problems/problems_LCR_048"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_048", "problems", problemLCR_048.Solve)
	TestEach(t, "148", "problems", problem148.Solve)
}
