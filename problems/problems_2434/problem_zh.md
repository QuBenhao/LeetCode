# 2434. 使用机器人打印字典序最小的字符串 [难度分: 1953.14]

<p>给你一个字符串&nbsp;<code>s</code>&nbsp;和一个机器人，机器人当前有一个空字符串&nbsp;<code>t</code>&nbsp;。执行以下操作之一，直到&nbsp;<code>s</code> 和&nbsp;<code>t</code>&nbsp;<strong>都变成空字符串：</strong></p>

<ul>
	<li>删除字符串&nbsp;<code>s</code>&nbsp;的 <strong>第一个</strong>&nbsp;字符，并将该字符给机器人。机器人把这个字符添加到 <code>t</code>&nbsp;的尾部。</li>
	<li>删除字符串&nbsp;<code>t</code>&nbsp;的&nbsp;<strong>最后一个</strong>&nbsp;字符，并将该字符给机器人。机器人将该字符写到纸上。</li>
</ul>

<p>请你返回纸上能写出的字典序最小的字符串。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>s = "zza"
<b>输出：</b>"azz"
<b>解释：</b>用 p 表示写出来的字符串。
一开始，p="" ，s="zza" ，t="" 。
执行第一个操作三次，得到 p="" ，s="" ，t="zza" 。
执行第二个操作三次，得到 p="azz" ，s="" ，t="" 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>s = "bac"
<b>输出：</b>"abc"
<b>解释：</b>用 p 表示写出来的字符串。
执行第一个操作两次，得到 p="" ，s="c" ，t="ba" 。
执行第二个操作两次，得到 p="ab" ，s="c" ，t="" 。
执行第一个操作，得到 p="ab" ，s="" ，t="c" 。
执行第二个操作，得到 p="abc" ，s="" ，t="" 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>s = "bdda"
<b>输出：</b>"addb"
<b>解释：</b>用 p 表示写出来的字符串。
一开始，p="" ，s="bdda" ，t="" 。
执行第一个操作四次，得到 p="" ，s="" ，t="bdda" 。
执行第二个操作四次，得到 p="addb" ，s="" ，t="" 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code>&nbsp;只包含小写英文字母。</li>
</ul>
