# 3791. Number of Balanced Integers in a Range 

<p>You are given two integers <code>low</code> and <code>high</code>.</p>

<p>An integer is called <strong>balanced</strong> if it satisfies <strong>both</strong> of the following conditions:</p>

<ul>
	<li>It contains <strong>at least</strong> two digits.</li>
	<li>The <strong>sum of digits at even positions</strong> is equal to the <strong>sum of digits at odd positions</strong> (the leftmost digit has position 1).</li>
</ul>

<p>Return an integer representing the number of balanced integers in the range <code>[low, high]</code> (both inclusive).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">low = 1, high = 100</span></p>

<p><strong>Output:</strong> <span class="example-io">9</span></p>

<p><strong>Explanation:</strong></p>

<p>The 9 balanced numbers between 1 and 100 are 11, 22, 33, 44, 55, 66, 77, 88, and 99.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">low = 120, high = 129</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>Only 121 is balanced because the sum of digits at even and odd positions are both 2.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">low = 1234, high = 1234</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>1234 is not balanced because the sum of digits at odd positions <code>(1 + 3 = 4)</code> does not equal the sum at even positions <code>(2 + 4 = 6)</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= low &lt;= high &lt;= 10<sup>15</sup></code></li>
</ul>
