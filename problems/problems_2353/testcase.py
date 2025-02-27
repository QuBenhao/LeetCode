from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['FoodRatings', 'highestRated', 'highestRated', 'changeRating', 'highestRated', 'changeRating', 'highestRated'], [[['kimchi', 'miso', 'sushi', 'moussaka', 'ramen', 'bulgogi'], ['korean', 'japanese', 'japanese', 'greek', 'japanese', 'korean'], [9, 12, 8, 15, 14, 7]], ['korean'], ['japanese'], ['sushi', 16], ['japanese'], ['ramen', 16], ['japanese']]], Output=[None, 'kimchi', 'ramen', None, 'sushi', None, 'ramen']))

	def get_testcases(self):
		return self.testcases
