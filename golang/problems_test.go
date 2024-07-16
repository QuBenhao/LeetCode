package golang

import (
	"leetCode/problems/problems_136"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "136", "problems", problem136.Solve)
}
