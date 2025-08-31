from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['aa', 'ab', 'ba', 'ac'], 'a'], Output=2))
		self.testcases.append(case(Input=[['aa', 'ab', 'ba'], 'a'], Output=1))
		self.testcases.append(case(Input=[['aa', 'ab', 'ba', 'ac'], 'b'], Output=0))

	def get_testcases(self):
		return self.testcases
