# 2912. Number of Ways to Reach Destination in the Grid

<p>You are given two integers <code>n</code> and <code>m</code> which represent the size of a <strong>1-indexed </strong>grid. You are also given an integer <code>k</code>, a <strong>1-indexed</strong> integer array <code>source</code> and a <strong>1-indexed</strong> integer array <code>dest</code>, where <code>source</code> and <code>dest</code> are in the form <code>[x, y]</code> representing a cell on the given grid.</p>

<p>You can move through the grid in the following way:</p>

<ul>
	<li>You can go from cell <code>[x<sub>1</sub>, y<sub>1</sub>]</code> to cell <code>[x<sub>2</sub>, y<sub>2</sub>]</code> if either <code>x<sub>1</sub> == x<sub>2</sub></code> or <code>y<sub>1</sub> == y<sub>2</sub></code>.</li>
	<li>Note that you <strong>can&#39;t</strong> move to the cell you are already in e.g. <code>x<sub>1</sub> == x<sub>2</sub></code> and <code>y<sub>1</sub> == y<sub>2</sub></code>.</li>
</ul>

<p>Return <em>the number of ways you can reach</em> <code>dest</code> <em>from</em> <code>source</code> <em>by moving through the grid</em> <strong>exactly</strong> <code>k</code> <em>times.</em></p>

<p>Since the answer may be very large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 3, m = 2, k = 2, source = [1,1], dest = [2,2]
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are 2 possible sequences of reaching [2,2] from [1,1]:
- [1,1] -&gt; [1,2] -&gt; [2,2]
- [1,1] -&gt; [2,1] -&gt; [2,2]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 3, m = 4, k = 3, source = [1,2], dest = [2,3]
<strong>Output:</strong> 9
<strong>Explanation:</strong> There are 9 possible sequences of reaching [2,3] from [1,2]:
- [1,2] -&gt; [1,1] -&gt; [1,3] -&gt; [2,3]
- [1,2] -&gt; [1,1] -&gt; [2,1] -&gt; [2,3]
- [1,2] -&gt; [1,3] -&gt; [3,3] -&gt; [2,3]
- [1,2] -&gt; [1,4] -&gt; [1,3] -&gt; [2,3]
- [1,2] -&gt; [1,4] -&gt; [2,4] -&gt; [2,3]
- [1,2] -&gt; [2,2] -&gt; [2,1] -&gt; [2,3]
- [1,2] -&gt; [2,2] -&gt; [2,4] -&gt; [2,3]
- [1,2] -&gt; [3,2] -&gt; [2,2] -&gt; [2,3]
- [1,2] -&gt; [3,2] -&gt; [3,3] -&gt; [2,3]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n, m &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k&nbsp;&lt;= 10<sup>5</sup></code></li>
	<li><code>source.length == dest.length == 2</code></li>
	<li><code>1 &lt;= source[1], dest[1] &lt;= n</code></li>
	<li><code>1 &lt;= source[2], dest[2] &lt;= m</code></li>
</ul>
