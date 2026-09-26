# 1190. 反转每对括号间的子串 [难度分: 1485.66]

<p>给出一个字符串&nbsp;<code>s</code>（仅含有小写英文字母和括号）。</p>

<p>请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。</p>

<p>注意，您的结果中 <strong>不应</strong> 包含任何括号。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "(abcd)"
<strong>输出：</strong>"dcba"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "(u(love)i)"
<strong>输出：</strong>"iloveu"
<strong>解释：</strong>先反转子字符串 "love" ，然后反转整个字符串。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "(ed(et(oc))el)"
<strong>输出：</strong>"leetcode"
<strong>解释：</strong>先反转子字符串 "oc" ，接着反转 "etco" ，然后反转整个字符串。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 2000</code></li>
	<li><code>s</code> 中只有小写英文字母和括号</li>
	<li>题目测试用例确保所有括号都是成对出现的</li>
</ul>
