from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['--X', 'X++', 'X++'], Output=1))
		self.testcases.append(case(Input=['++X', '++X', 'X++'], Output=3))
		self.testcases.append(case(Input=['X++', '++X', '--X', 'X--'], Output=0))

	def get_testcases(self):
		return self.testcases
