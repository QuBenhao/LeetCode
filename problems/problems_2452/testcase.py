from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['word', 'note', 'ants', 'wood'], ['wood', 'joke', 'moat']], Output=['word', 'note', 'wood']))
		self.testcases.append(case(Input=[['yes'], ['not']], Output=[]))

	def get_testcases(self):
		return self.testcases
