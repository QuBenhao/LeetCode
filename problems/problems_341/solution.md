# [Python] An iterator should point to data rather than copy it

> Author: Benhao
> Date: 2021-03-23
> Upvotes: 1
> Tags: Python

---

### Approach
Start with an approach that points to the original data rather than copying it.
Each list position contains either a number or another list.
A number is exactly what we need.
For a list, find the next number within it.
If that list has no next number, move to the next element in its parent list.

I also implemented NestedInteger for anyone who wants to test locally.

### Code

```python
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger(object):
    def __init__(self, item=None):
        self._integer = None
        self._list = None
        if item is not None:
            if type(item) == int:
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
        while self.iter < len(self.nestedList)-1:
            self.iter += 1
            if self.nestedList[self.iter].isInteger():
                return True
            self.inner = NestedIterator(self.nestedList[self.iter].getList())
            if self.inner.hasNext():
                return True
            # current list has no integer, we don't know the next list yet, reset to None
            self.inner = None
        return False


# Your NestedIterator object will be instantiated and called as such:
# change test_input here
test_input = [[1,1],2,[1,1]]
nestedList = []
for item in test_input:
    nestedList.append(NestedInteger(item))
i, v = NestedIterator(nestedList), []
while i.hasNext(): 
    v.append(i.next())
print(v)
```
