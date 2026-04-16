# [Python/Java/JavaScript] 迭代器模拟

> Author: Benhao
> Date: 2021-10-04
> Upvotes: 24
> Tags: Java, JavaScript, Python, Python3

---

### 解题思路
存储上一个peek的元素，如果有就在peek时直接返回，不移动指针；next的时候清空peek的元素。

### 代码
```Python3 []
class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        self.pk = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.pk is None:
            self.pk = self.iter.next()
        return self.pk

    def next(self):
        """
        :rtype: int
        """
        if self.pk is not None:
            val = self.pk
            self.pk = None
            return val
        return self.iter.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.pk is not None or self.iter.hasNext()
```
```Java []
class PeekingIterator implements Iterator<Integer> {
    private Iterator<Integer> iter;
    private Integer element;
	public PeekingIterator(Iterator<Integer> iterator) {
	    // initialize any member here.
	    iter = iterator;
        element = null;
	}
	
    // Returns the next element in the iteration without advancing the iterator.
	public Integer peek() {
        if(element == null)
            element = iter.next();
        return element;
	}
	
	// hasNext() and next() should behave the same as in the Iterator interface.
	// Override them if needed.
	@Override
	public Integer next() {
	    if(element != null){
            Integer val = element;
            element = null;
            return val;
        }
        return iter.next();
	}
	
	@Override
	public boolean hasNext() {
        return element != null || iter.hasNext();   
	}
}
```
```JavaScript []
let iter;
let element;
/**
 * @param {Iterator} iterator
 */
var PeekingIterator = function(iterator) {
    iter = iterator;
    element = null;
};

/**
 * @return {number}
 */
PeekingIterator.prototype.peek = function() {
    if(element == null)
        element = iter.next();
    return element;
};

/**
 * @return {number}
 */
PeekingIterator.prototype.next = function() {
    if(element != null){
        const val = element;
        element = null;
        return val;
    }
    return iter.next();
};

/**
 * @return {boolean}
 */
PeekingIterator.prototype.hasNext = function() {
    return element != null || iter.hasNext();  
};

```