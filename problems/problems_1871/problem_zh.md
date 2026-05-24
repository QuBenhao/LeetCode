# 1871. 跳跃游戏 VII [难度分: 1896.14]

<p>给你一个下标从 <strong>0 </strong>开始的二进制字符串 <code>s</code> 和两个整数 <code>minJump</code> 和 <code>maxJump</code> 。一开始，你在下标 <code>0</code> 处，且该位置的值一定为 <code>'0'</code> 。当同时满足如下条件时，你可以从下标 <code>i</code> 移动到下标 <code>j</code> 处：</p>

<ul>
	<li><code>i + minJump <= j <= min(i + maxJump, s.length - 1)</code> 且</li>
	<li><code>s[j] == '0'</code>.</li>
</ul>

<p>如果你可以到达 <code>s</code> 的下标<i> </i><code>s.length - 1</code> 处，请你返回 <code>true</code> ，否则返回 <code>false</code> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>s = "<strong>0</strong>11<strong>0</strong>1<strong>0</strong>", minJump = 2, maxJump = 3
<b>输出：</b>true
<strong>解释：</strong>
第一步，从下标 0 移动到下标 3 。
第二步，从下标 3 移动到下标 5 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>s = "01101110", minJump = 2, maxJump = 3
<b>输出：</b>false
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 <= s.length <= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> 要么是 <code>'0'</code> ，要么是 <code>'1'</code></li>
	<li><code>s[0] == '0'</code></li>
	<li><code>1 <= minJump <= maxJump < s.length</code></li>
</ul>
