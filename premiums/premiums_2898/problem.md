# 2898. Maximum Linear Stock Score

<p>Given a <strong>1-indexed</strong> integer array <code>prices</code>, where <code>prices[i]</code> is the price of a particular stock on the <code>i<sup>th</sup></code> day, your task is to select some of the elements of <code>prices</code> such that your selection is <strong>linear</strong>.</p>

<p>A selection <code>indexes</code>, where <code>indexes</code> is a <strong>1-indexed</strong> integer array of length <code>k</code> which is a subsequence of the array <code>[1, 2, ..., n]</code>, is <strong>linear</strong> if:</p>

<ul>
	<li>For every <code>1 &lt; j &lt;= k</code>, <code>prices[indexes[j]] - prices[indexes[j - 1]] == indexes[j] - indexes[j - 1]</code>.</li>
</ul>

<p>A <b>subsequence</b> is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.</p>

<p>The <strong>score</strong> of a selection <code>indexes</code>, is equal to the sum of the following array: <code>[prices[indexes[1]], prices[indexes[2]], ..., prices[indexes[k]]</code>.</p>

<p>Return <em>the <strong>maximum</strong> <strong>score</strong> that a linear selection can have</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> prices = [1,5,3,7,8]
<strong>Output:</strong> 20
<strong>Explanation:</strong> We can select the indexes [2,4,5]. We show that our selection is linear:
For j = 2, we have:
indexes[2] - indexes[1] = 4 - 2 = 2.
prices[4] - prices[2] = 7 - 5 = 2.
For j = 3, we have:
indexes[3] - indexes[2] = 5 - 4 = 1.
prices[5] - prices[4] = 8 - 7 = 1.
The sum of the elements is: prices[2] + prices[4] + prices[5] = 20.
It can be shown that the maximum sum a linear selection can have is 20.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> prices = [5,6,7,8,9]
<strong>Output:</strong> 35
<strong>Explanation:</strong> We can select all of the indexes [1,2,3,4,5]. Since each element has a difference of exactly 1 from its previous element, our selection is linear.
The sum of all the elements is 35 which is the maximum possible some out of every selection.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= prices.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= prices[i] &lt;= 10<sup>9</sup></code></li>
</ul>
