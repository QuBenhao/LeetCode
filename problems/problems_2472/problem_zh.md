# 2472. 不重叠回文子字符串的最大数目 [难度分: 2013.44]

<p>给你一个字符串 <code>s</code> 和一个 <strong>正</strong> 整数 <code>k</code> 。</p>

<p>从字符串 <code>s</code> 中选出一组满足下述条件且 <strong>不重叠</strong> 的子字符串：</p>

<ul>
	<li>每个子字符串的长度 <strong>至少</strong> 为 <code>k</code> 。</li>
	<li>每个子字符串是一个 <strong>回文串</strong> 。</li>
</ul>

<p>返回最优方案中能选择的子字符串的 <strong>最大</strong> 数目。</p>

<p><strong>子字符串</strong> 是字符串中一个连续的字符序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1 ：</strong></p>

<pre>
<strong>输入：</strong>s = "abaccdbbd", k = 3
<strong>输出：</strong>2
<strong>解释：</strong>可以选择 s = "<em><strong>aba</strong></em>cc<em><strong>dbbd</strong></em>" 中斜体加粗的子字符串。"aba" 和 "dbbd" 都是回文，且长度至少为 k = 3 。
可以证明，无法选出两个以上的有效子字符串。
</pre>

<p><strong>示例 2 ：</strong></p>

<pre>
<strong>输入：</strong>s = "adbcda", k = 2
<strong>输出：</strong>0
<strong>解释：</strong>字符串中不存在长度至少为 2 的回文子字符串。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= s.length &lt;= 2000</code></li>
	<li><code>s</code> 仅由小写英文字母组成</li>
</ul>
