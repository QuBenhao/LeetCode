# 2734. 执行子串操作后的字典序最小字符串 [难度分: 1405.12]

<p>给你一个仅由小写英文字母组成的字符串 <code>s</code> 。在一步操作中，你可以完成以下行为：</p>

<ul>
	<li>选择&nbsp;<code>s</code> 的任一非空子字符串，可能是整个字符串，接着将字符串中的每一个字符替换为英文字母表中的前一个字符。例如，'b' 用 'a' 替换，'a' 用 'z' 替换。</li>
</ul>

<p>返回执行上述操作 <strong>恰好一次</strong> 后可以获得的 <strong>字典序最小</strong> 的字符串。</p>

<p><strong>子字符串</strong> 是字符串中的一个连续字符序列。</p>
现有长度相同的两个字符串 <code>x</code> 和 字符串 <code>y</code> ，在满足&nbsp;<code>x[i] != y[i]</code> 的第一个位置 <code>i</code> 上，如果&nbsp; <code>x[i]</code> 在字母表中先于 <code>y[i]</code> 出现，则认为字符串 <code>x</code> 比字符串 <code>y</code> <strong>字典序更小</strong> 。

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "cbabc"
<strong>输出：</strong>"baabc"
<strong>解释：</strong>我们选择从下标 0 开始、到下标 1 结束的子字符串执行操作。 
可以证明最终得到的字符串是字典序最小的。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "acbbc"
<strong>输出：</strong>"abaab"
<strong>解释：</strong>我们选择从下标 1 开始、到下标 4 结束的子字符串执行操作。
可以证明最终得到的字符串是字典序最小的。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "leetcode"
<strong>输出：</strong>"kddsbncd"
<strong>解释：</strong>我们选择整个字符串执行操作。
可以证明最终得到的字符串是字典序最小的。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 3 * 10<sup>5</sup></code></li>
	<li><code>s</code> 仅由小写英文字母组成</li>
</ul>
