# 761. 特殊的二进制字符串 [难度分: 2292.14]

<p><strong>特殊的二进制字符串</strong> 是具有以下两个性质的二进制序列：</p>

<ul>
	<li><code>0</code> 的数量与 <code>1</code> 的数量相等。</li>
	<li>二进制序列的每一个前缀码中 <code>1</code> 的数量要大于等于 <code>0</code> 的数量。</li>
</ul>

<p>给定一个特殊的二进制字符串&nbsp;<code>s</code>。</p>

<p>一次移动操作包括选择字符串 <code>s</code> 中的两个连续的、非空的、特殊子串，并交换它们。两个字符串是连续的，如果第一个字符串的最后一个字符与第二个字符串的第一个字符的索引相差正好为 1。</p>

<p>返回在字符串上应用任意次操作后可能得到的字典序最大的字符串。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> S = "11011000"
<strong>输出:</strong> "11100100"
<strong>解释:</strong>
将子串 "10" （在 s[1] 出现） 和 "1100" （在 s[3] 出现）进行交换。
这是在进行若干次操作后按字典序排列最大的结果。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>s = "10"
<b>输出：</b>"10"
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 50</code></li>
	<li><code>s[i]</code>&nbsp;为&nbsp;<code>'0'</code> 或&nbsp;<code>'1'</code>。</li>
	<li><code>s</code>&nbsp;是一个特殊的二进制字符串。</li>
</ul>
