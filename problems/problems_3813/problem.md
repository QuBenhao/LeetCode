# 3813. Vowel-Consonant Score 

<p>You are given a string <code>s</code> consisting of lowercase English letters, spaces, and digits.</p>

<p>Let <code>v</code> be the number of vowels in <code>s</code> and <code>c</code> be the number of consonants in <code>s</code>.</p>

<p>A vowel is one of the letters <code>&#39;a&#39;</code>, <code>&#39;e&#39;</code>, <code>&#39;i&#39;</code>, <code>&#39;o&#39;</code>, or <code>&#39;u&#39;</code>, while any other letter in the English alphabet is considered a consonant.</p>

<p>The <strong>score</strong> of the string <code>s</code> is defined as follows:</p>

<ul>
	<li>If <code>c &gt; 0</code>, the <code>score = floor(v / c)</code> where floor denotes <strong>rounding down</strong> to the nearest integer.</li>
	<li>Otherwise, the <code>score = 0</code>.</li>
</ul>

<p>Return an integer denoting the score of the string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;cooear&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>The string <code>s = &quot;cooear&quot;</code> contains <code>v = 4</code> vowels <code>(&#39;o&#39;, &#39;o&#39;, &#39;e&#39;, &#39;a&#39;)</code> and <code>c = 2</code> consonants <code>(&#39;c&#39;, &#39;r&#39;)</code>.</p>

<p>The score is <code>floor(v / c) = floor(4 / 2) = 2</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;axeyizou&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>The string <code>s = &quot;axeyizou&quot;</code> contains <code>v = 5</code> vowels <code>(&#39;a&#39;, &#39;e&#39;, &#39;i&#39;, &#39;o&#39;, &#39;u&#39;)</code> and <code>c = 3</code> consonants <code>(&#39;x&#39;, &#39;y&#39;, &#39;z&#39;)</code>.</p>

<p>The score is <code>floor(v / c) = floor(5 / 3) = 1</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;au 123&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>The string <code>s = &quot;au 123&quot;</code> contains no consonants <code>(c = 0)</code>, so the score is 0.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> consists of lowercase English letters, spaces and digits.</li>
</ul>
