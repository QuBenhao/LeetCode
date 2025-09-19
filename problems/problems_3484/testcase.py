from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['Spreadsheet', 'getValue', 'setCell', 'getValue', 'setCell', 'getValue', 'resetCell', 'getValue'], [[3], ['=5+7'], ['A1', 10], ['=A1+6'], ['B2', 15], ['=A1+B2'], ['A1'], ['=A1+B2']]], Output=[None, 12, None, 16, None, 25, None, 15]))
		self.testcases.append(case(Input=[["Spreadsheet","getValue"],[[934],["=3138+15425"]]], Output=[None,18563]))

	def get_testcases(self):
		return self.testcases
