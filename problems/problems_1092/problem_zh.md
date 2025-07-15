# 1092. 最短公共超序列 [难度分: 1976.72]

<p>给你两个字符串&nbsp;<code>str1</code> 和&nbsp;<code>str2</code>，返回同时以&nbsp;<code>str1</code>&nbsp;和&nbsp;<code>str2</code>&nbsp;作为 <strong>子序列</strong> 的最短字符串。如果答案不止一个，则可以返回满足条件的 <strong>任意一个</strong> 答案。</p>

<p>如果从字符串 <code>t</code> 中删除一些字符（也可能不删除），可以得到字符串 <code>s</code> ，那么 <code>s</code> 就是 t 的一个子序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>str1 = "abac", str2 = "cab"
<strong>输出：</strong>"cabac"
<strong>解释：</strong>
str1 = "abac" 是 "cabac" 的一个子串，因为我们可以删去 "cabac" 的第一个 "c"得到 "abac"。 
str2 = "cab" 是 "cabac" 的一个子串，因为我们可以删去 "cabac" 末尾的 "ac" 得到 "cab"。
最终我们给出的答案是满足上述属性的最短字符串。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>str1 = "aaaaaaaa", str2 = "aaaaaaaa"
<strong>输出：</strong>"aaaaaaaa"
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= str1.length, str2.length &lt;= 1000</code></li>
	<li><code>str1</code> 和&nbsp;<code>str2</code>&nbsp;都由小写英文字母组成。</li>
</ul>
