import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        # Your NestedIterator object will be instantiated and called as such:
        nested_list = []
        for item in test_input:
            nested_list.append(NestedInteger(item))
        i, v = NestedIterator(nested_list), []
        while i.hasNext():
            v.append(i.next())
        return v


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger(object):
    def __init__(self, item=None):
        self._integer = None
        self._list = None
        if item is not None:
            if isinstance(item, int):
                self._integer = item
            else:
                l = []
                for i in item:
                    l.append(NestedInteger(i))
                self._list = l

    def __len__(self):
        if self._list:
            return len(self._list)

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        return self._integer is not None

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        return self._integer

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        return self._list


class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.nestedList = nestedList
        # pointer to the item in the nestedList
        self.iter = -1
        # pointer to the item in a list in the nestedList
        self.inner = None

    def next(self):
        """
        :rtype: int
        """
        # return inner item from list before next item in the nestedList
        if self.inner:
            return self.inner.next()
        return self.nestedList[self.iter].getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        # There is a inner list currently
        if self.inner and self.inner.hasNext():
            return True
        self.inner = None
        # find the next integer or a list contain integer
        while self.iter < len(self.nestedList) - 1:
            self.iter += 1
            if self.nestedList[self.iter].isInteger():
                return True
            self.inner = NestedIterator(self.nestedList[self.iter].getList())
            if self.inner.hasNext():
                return True
            # current list has no integer, we don't know the next list yet, reset to None
            self.inner = None
        return False
