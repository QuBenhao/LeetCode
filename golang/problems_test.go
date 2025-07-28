package golang

import (
	problem3628 "leetCode/problems/problems_3628"
	problem3629 "leetCode/problems/problems_3629"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "3628", "problems", problem3628.Solve)
	TestEach(t, "3629", "problems", problem3629.Solve)
}
