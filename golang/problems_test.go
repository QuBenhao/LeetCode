package golang

import (
	"leetCode/problems/problems_416"
	"leetCode/problems/problems_84"
	"leetCode/problems/problems_LCR_022"
	"leetCode/problems/problems_LCR_063"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_063", "problems", problemLCR_063.Solve)
	TestEach(t, "LCR_022", "problems", problemLCR_022.Solve)
	TestEach(t, "84", "problems", problem84.Solve)
	TestEach(t, "416", "problems", problem416.Solve)
}
