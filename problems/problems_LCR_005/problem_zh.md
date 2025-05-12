# LCR 005. 最大单词长度乘积 

<p>给定一个字符串数组&nbsp;<code>words</code>，请计算当两个字符串 <code>words[i]</code> 和 <code>words[j]</code> 不包含相同字符时，它们长度的乘积的最大值。假设字符串中只包含英语的小写字母。如果没有不包含相同字符的一对字符串，返回 0。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>words = [&quot;abcw&quot;,&quot;baz&quot;,&quot;foo&quot;,&quot;bar&quot;,&quot;fxyz&quot;,&quot;abcdef&quot;]
<strong>输出：</strong>16 
<strong>解释：</strong>这两个单词为<strong> </strong>&quot;abcw&quot;, &quot;fxyz&quot;。它们不包含相同字符，且长度的乘积最大。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>words = [&quot;a&quot;,&quot;ab&quot;,&quot;abc&quot;,&quot;d&quot;,&quot;cd&quot;,&quot;bcd&quot;,&quot;abcd&quot;]
<strong>输出：</strong>4 
<strong>解释：</strong>这两个单词为 &quot;ab&quot;, &quot;cd&quot;。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>words = [&quot;a&quot;,&quot;aa&quot;,&quot;aaa&quot;,&quot;aaaa&quot;]
<strong>输出：</strong>0 
<strong>解释：</strong>不存在这样的两个单词。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= words.length &lt;= 1000</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 1000</code></li>
	<li><code>words[i]</code>&nbsp;仅包含小写字母</li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 318&nbsp;题相同：<a href="https://leetcode-cn.com/problems/maximum-product-of-word-lengths/">https://leetcode-cn.com/problems/maximum-product-of-word-lengths/</a></p>
