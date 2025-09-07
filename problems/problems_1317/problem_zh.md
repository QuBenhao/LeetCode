# 1317. 将整数转换为两个无零整数的和 [难度分: 1277.83]

<p>「无零整数」是十进制表示中 <strong>不含任何 0</strong>&nbsp;的正整数。</p>

<p>给你一个整数&nbsp;<code>n</code>，请你返回一个 <strong>由两个整数组成的列表</strong> <code>[a, b]</code>，满足：</p>

<ul>
	<li><code>a</code> 和 <code>b</code>&nbsp;都是无零整数</li>
	<li><code>a + b = n</code></li>
</ul>

<p>题目数据保证至少有一个有效的解决方案。</p>

<p>如果存在多个有效解决方案，你可以返回其中任意一个。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 2
<strong>输出：</strong>[1,1]
<strong>解释：</strong>a = 1, b = 1。a + b = n 并且 a 和 b 的十进制表示形式都不包含任何 0。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 11
<strong>输出：</strong>[2,9]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 10000
<strong>输出：</strong>[1,9999]
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>n = 69
<strong>输出：</strong>[1,68]
</pre>

<p><strong>示例 5：</strong></p>

<pre>
<strong>输入：</strong>n = 1010
<strong>输出：</strong>[11,999]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 10<sup>4</sup></code></li>
</ul>
