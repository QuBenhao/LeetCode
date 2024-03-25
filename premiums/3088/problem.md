# 3088. Make String Anti-palindrome

<p>We call a string <code>s</code> of <strong>even</strong> length <code>n</code> an <strong>anti-palindrome</strong> if for each index <code>0 &lt;= i &lt; n</code>, <code>s[i] != s[n - i - 1]</code>.</p>

<p>Given a string <code>s</code>, your task is to make <code>s</code> an <strong>anti-palindrome</strong> by doing <strong>any</strong> number of operations (including zero).</p>

<p>In one operation, you can select two characters from <code>s</code> and swap them.</p>

<p>Return <em>the resulting string. If multiple strings meet the conditions, return the <span data-keyword="lexicographically-smaller-string">lexicographically smallest</span> one. If it can&#39;t be made into an anti-palindrome, return </em><code>&quot;-1&quot;</code><em>.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;abca&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;aabc&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p><code>&quot;aabc&quot;</code> is an anti-palindrome string since <code>s[0] != s[3]</code> and <code>s[1] != s[2]</code>. Also, it is a rearrangement of <code>&quot;abca&quot;</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;abba&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;aabb&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p><code>&quot;aabb&quot;</code> is an anti-palindrome string since <code>s[0] != s[3]</code> and <code>s[1] != s[2]</code>. Also, it is a rearrangement of <code>&quot;abba&quot;</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;cccd&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;-1&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>You can see that no matter how you rearrange the characters of <code>&quot;cccd&quot;</code>, either <code>s[0] == s[3]</code> or <code>s[1] == s[2]</code>. So it can not form an anti-palindrome string.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s.length % 2 == 0</code></li>
	<li><code>s</code> consists only of lowercase English letters.</li>
</ul>
