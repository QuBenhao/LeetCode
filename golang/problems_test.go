package golang

import (
	"leetCode/problems/problems_226"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "226", "problems", problem226.Solve)
}
