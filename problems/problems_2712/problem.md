# 2712. Minimum Cost to Make All Characters Equal [Rating: 1791.03]

<p>You are given a <strong>0-indexed</strong> binary string <code>s</code> of length <code>n</code> on which you can apply two types of operations:</p>

<ul>
	<li>Choose an index <code>i</code> and invert all characters from&nbsp;index <code>0</code> to index <code>i</code>&nbsp;(both inclusive), with a cost of <code>i + 1</code></li>
	<li>Choose an index <code>i</code> and invert all characters&nbsp;from&nbsp;index <code>i</code> to index <code>n - 1</code>&nbsp;(both inclusive), with a cost of <code>n - i</code></li>
</ul>

<p>Return <em>the <strong>minimum cost </strong>to make all characters of the string <strong>equal</strong></em>.</p>

<p><strong>Invert</strong> a character means&nbsp;if its value is &#39;0&#39; it becomes &#39;1&#39; and vice-versa.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;0011&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> Apply the second operation with <code>i = 2</code> to obtain <code>s = &quot;0000&quot; for a cost of 2</code>. It can be shown that 2 is the minimum cost to make all characters equal.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;010101&quot;
<strong>Output:</strong> 9
<strong>Explanation:</strong> Apply the first operation with i = 2 to obtain s = &quot;101101&quot; for a cost of 3.
Apply the first operation with i = 1 to obtain s = &quot;011101&quot; for a cost of 2. 
Apply the first operation with i = 0 to obtain s = &quot;111101&quot; for a cost of 1. 
Apply the second operation with i = 4 to obtain s = &quot;111110&quot; for a cost of 2.
Apply the second operation with i = 5 to obtain s = &quot;111111&quot; for a cost of 1. 
The total cost to make all characters equal is 9. It can be shown that 9 is the minimum cost to make all characters equal.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length == n &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> is either <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code></li>
</ul>
