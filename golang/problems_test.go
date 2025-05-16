package golang

import (
	"leetCode/problems/problems_LCR_057"
	"leetCode/problems/problems_LCR_118"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_057", "problems", problemLCR_057.Solve)
	TestEach(t, "LCR_118", "problems", problemLCR_118.Solve)
}
