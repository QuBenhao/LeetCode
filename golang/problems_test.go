package golang

import (
	problem3648 "leetCode/problems/problems_3648"
	problem3649 "leetCode/problems/problems_3649"
	problem3650 "leetCode/problems/problems_3650"
	problem3651 "leetCode/problems/problems_3651"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "3648", "problems", problem3648.Solve)
	TestEach(t, "3649", "problems", problem3649.Solve)
	TestEach(t, "3650", "problems", problem3650.Solve)
	TestEach(t, "3651", "problems", problem3651.Solve)
}
