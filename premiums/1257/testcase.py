from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[['Earth', 'North America', 'South America'], ['North America', 'United States', 'Canada'], ['United States', 'New York', 'Boston'], ['Canada', 'Ontario', 'Quebec'], ['South America', 'Brazil']], 'Quebec', 'New York'], Output="North America"))
		self.testcases.append(case(Input=[[['Earth', 'North America', 'South America'], ['North America', 'United States', 'Canada'], ['United States', 'New York', 'Boston'], ['Canada', 'Ontario', 'Quebec'], ['South America', 'Brazil']], 'Canada', 'South America'], Output="Earth"))

	def get_testcases(self):
		return self.testcases
