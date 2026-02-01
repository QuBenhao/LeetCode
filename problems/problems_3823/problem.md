# 3823. Reverse Letters Then Special Characters in a String 

<p>You are given a string <code>s</code> consisting of lowercase English letters and special characters.</p>

<p>Your task is to perform these <strong>in order</strong>:</p>

<ul>
	<li><strong>Reverse</strong> the <strong>lowercase letters</strong> and place them back into the positions originally occupied by letters.</li>
	<li><strong>Reverse</strong> the <strong>special characters</strong> and place them back into the positions originally occupied by special characters.</li>
</ul>

<p>Return the resulting string after performing the reversals.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;</span>)ebc#da@f(<span class="example-io">&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;</span>(fad@cb#e)<span class="example-io">&quot;</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The letters in the string are <code>[&#39;e&#39;, &#39;b&#39;, &#39;c&#39;, &#39;d&#39;, &#39;a&#39;, &#39;f&#39;]</code>:
	<ul>
		<li>Reversing them gives <code>[&#39;f&#39;, &#39;a&#39;, &#39;d&#39;, &#39;c&#39;, &#39;b&#39;, &#39;e&#39;]</code></li>
		<li><code>s</code> becomes <code>&quot;)fad#cb@e(&quot;</code></li>
	</ul>
	</li>
	<li>​​​​​​​The special characters in the string are <code>[&#39;)&#39;, &#39;#&#39;, &#39;@&#39;, &#39;(&#39;]</code>:
	<ul>
		<li>Reversing them gives <code>[&#39;(&#39;, &#39;@&#39;, &#39;#&#39;, &#39;)&#39;]</code></li>
		<li><code>s</code> becomes <code><span class="example-io">&quot;</span>(fad@cb#e)<span class="example-io">&quot;</span></code></li>
	</ul>
	</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;z&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;z&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>The string contains only one letter, and reversing it does not change the string. There are no special characters.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;!@#$%^&amp;*()&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;</span>)(*&amp;^%$#@!<span class="example-io">&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>The string contains no letters. The string contains all special characters, so reversing the special characters reverses the whole string.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> consists only of lowercase English letters and the special characters in <code>&quot;!@#$%^&amp;*()&quot;</code>.</li>
</ul>
