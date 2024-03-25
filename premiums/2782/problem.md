# 2782. Number of Unique Categories

<p>You are given an integer <code>n</code> and an object <code>categoryHandler</code> of class <code>CategoryHandler</code>.</p>

<p>There are <code>n&nbsp;</code>elements, numbered from <code>0</code> to <code>n - 1</code>. Each element has a category, and your task is to find the number of unique categories.</p>

<p>The class <code>CategoryHandler</code> contains the following function, which may help you:</p>

<ul>
	<li><code>boolean haveSameCategory(integer a, integer b)</code>: Returns <code>true</code> if <code>a</code> and <code>b</code> are in the same category and <code>false</code> otherwise. Also, if either <code>a</code> or <code>b</code> is not a valid number (i.e. it&#39;s greater than or equal to <code>n</code>or less than <code>0</code>), it returns <code>false</code>.</li>
</ul>

<p>Return <em>the number of unique categories.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 6, categoryHandler = [1,1,2,2,3,3]
<strong>Output:</strong> 3
<strong>Explanation:</strong> There are 6 elements in this example. The first two elements belong to category 1, the second two belong to category 2, and the last two elements belong to category 3. So there are 3 unique categories.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 5, categoryHandler = [1,2,3,4,5]
<strong>Output:</strong> 5
<strong>Explanation:</strong> There are 5 elements in this example. Each element belongs to a unique category. So there are 5 unique categories.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 3, categoryHandler = [1,1,1]
<strong>Output:</strong> 1
<strong>Explanation:</strong> There are 3 elements in this example. All of them belong to one category. So there is only 1 unique category.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 100</code></li>
</ul>
