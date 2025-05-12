package golang

import (
	"leetCode/problems/problems_LCR_005"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_005", "problems", problemLCR_005.Solve)
}
