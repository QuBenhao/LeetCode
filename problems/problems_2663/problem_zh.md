# 2663. 字典序最小的美丽字符串 [难度分: 2415.74]

<p>如果一个字符串满足以下条件，则称其为 <strong>美丽字符串</strong> ：</p>

<ul>
	<li>它由英语小写字母表的前 <code>k</code> 个字母组成。</li>
	<li>它不包含任何长度为 <code>2</code> 或更长的回文子字符串。</li>
</ul>

<p>给你一个长度为 <code>n</code> 的美丽字符串 <code>s</code> 和一个正整数 <code>k</code> 。</p>

<p>请你找出并返回一个长度为 <code>n</code> 的美丽字符串，该字符串还满足：在字典序大于 <code>s</code> 的所有美丽字符串中字典序最小。如果不存在这样的字符串，则返回一个空字符串。</p>

<p>对于长度相同的两个字符串 <code>a</code> 和 <code>b</code> ，如果字符串 <code>a</code> 在与字符串 <code>b</code> 不同的第一个位置上的字符字典序更大，则字符串 <code>a</code> 的字典序大于字符串 <code>b</code> 。</p>

<ul>
	<li>例如，<code>"abcd"</code> 的字典序比 <code>"abcc"</code> 更大，因为在不同的第一个位置（第四个字符）上 <code>d</code> 的字典序大于 <code>c</code> 。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "abcz", k = 26
<strong>输出：</strong>"abda"
<strong>解释：</strong>字符串 "abda" 既是美丽字符串，又满足字典序大于 "abcz" 。
可以证明不存在字符串同时满足字典序大于 "abcz"、美丽字符串、字典序小于 "abda" 这三个条件。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "dc", k = 4
<strong>输出：</strong>""
<strong>解释：</strong>可以证明，不存在既是美丽字符串，又字典序大于 "dc" 的字符串。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n == s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>4 &lt;= k &lt;= 26</code></li>
	<li><code>s</code> 是一个美丽字符串</li>
</ul>
