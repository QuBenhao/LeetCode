# 3557. Find Maximum Number of Non Intersecting Substrings 

<p>You are given a string <code>word</code>.</p>

<p>Return the <strong>maximum</strong> number of non-intersecting <strong>substrings</strong> of word that are at <strong>least</strong> four characters long and start and end with the same letter.</p>

<p>A <strong>substring</strong> is a contiguous <b>non-empty</b> sequence of characters within a string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">word = &quot;abcdeafdef&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>The two substrings are <code>&quot;abcdea&quot;</code> and <code>&quot;fdef&quot;</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">word = &quot;bcdaaaab&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>The only substring is <code>&quot;aaaa&quot;</code>. Note that we cannot <strong>also</strong> choose <code>&quot;bcdaaaab&quot;</code> since it intersects with the other substring.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>word</code> consists only of lowercase English letters.</li>
</ul>
