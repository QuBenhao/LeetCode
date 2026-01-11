# 3803. Count Residue Prefixes 

<p>You are given a string <code>s</code> consisting only of lowercase English letters.</p>

<p>A <strong>prefix</strong> of <code>s</code> is called a <strong>residue</strong> if the number of <strong>distinct characters</strong> in the <strong>prefix</strong> is equal to <code>len(prefix) % 3</code>.</p>

<p>Return the count of <strong>residue</strong> prefixes in <code>s</code>.</p>
A <strong>prefix</strong> of a string is a <strong>non-empty substring</strong> that starts from the beginning of the string and extends to any point within it.
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;abc&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong>​​​​​​​</p>

<ul>
	<li>Prefix <code>&quot;a&quot;</code> has 1 distinct character and length modulo 3 is 1, so it is a residue.</li>
	<li>Prefix <code>&quot;ab&quot;</code> has 2 distinct characters and length modulo 3 is 2, so it is a residue.</li>
	<li>Prefix <code>&quot;abc&quot;</code> does not satisfy the condition. Thus, the answer is 2.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;dd&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Prefix <code>&quot;d&quot;</code> has 1 distinct character and length modulo 3 is 1, so it is a residue.</li>
	<li>Prefix <code>&quot;dd&quot;</code> has 1 distinct character but length modulo 3 is 2, so it is not a residue. Thus, the answer is 1.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;bob&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Prefix <code>&quot;b&quot;</code> has 1 distinct character and length modulo 3 is 1, so it is a residue.</li>
	<li>Prefix <code>&quot;bo&quot;</code> has 2 distinct characters and length mod 3 is 2, so it is a residue. Thus, the answer is 2.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> contains only lowercase English letters.</li>
</ul>
