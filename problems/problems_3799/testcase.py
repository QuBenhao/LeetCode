from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['able', 'area', 'echo', 'also'], Output=[['able', 'area', 'echo', 'also'], ['area', 'able', 'also', 'echo']]))
		self.testcases.append(case(Input=['code', 'cafe', 'eden', 'edge'], Output=[]))

	def get_testcases(self):
		return self.testcases
