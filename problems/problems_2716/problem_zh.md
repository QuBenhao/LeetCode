# 2716. 最小化字符串长度 [难度分: 1242.94]

<p>给你一个下标从 <strong>0</strong> 开始的字符串 <code>s</code> ，重复执行下述操作 <strong>任意</strong> 次：</p>

<ul>
	<li>在字符串中选出一个下标 <code>i</code> ，并使 <code>c</code> 为字符串下标 <code>i</code> 处的字符。并在 <code>i</code> <strong>左侧</strong>（如果有）和 <strong>右侧</strong>（如果有）各 <strong>删除 </strong>一个距离 <code>i</code> <strong>最近</strong> 的字符 <code>c</code> 。</li>
</ul>

<p>请你通过执行上述操作任意次，使 <code>s</code> 的长度 <strong>最小化</strong> 。</p>

<p>返回一个表示 <strong>最小化</strong> 字符串的长度的整数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "aaabc"
<strong>输出：</strong>3
<strong>解释：</strong>在这个示例中，s 等于 "aaabc" 。我们可以选择位于下标 1 处的字符 'a' 开始。接着删除下标 1 左侧最近的那个 'a'（位于下标 0）以及下标 1 右侧最近的那个 'a'（位于下标 2）。执行操作后，字符串变为 "abc" 。继续对字符串执行任何操作都不会改变其长度。因此，最小化字符串的长度是 3 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "cbbd"
<strong>输出：</strong>3
<strong>解释：</strong>我们可以选择位于下标 1 处的字符 'b' 开始。下标 1 左侧不存在字符 'b' ，但右侧存在一个字符 'b'（位于下标 2），所以会删除位于下标 2 的字符 'b' 。执行操作后，字符串变为 "cbd" 。继续对字符串执行任何操作都不会改变其长度。因此，最小化字符串的长度是 3 。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "dddaaa"
<strong>输出：</strong>2
<strong>解释：</strong>我们可以选择位于下标 1 处的字符 'd' 开始。接着删除下标 1 左侧最近的那个 'd'（位于下标 0）以及下标 1 右侧最近的那个 'd'（位于下标 2）。执行操作后，字符串变为 "daaa" 。继续对新字符串执行操作，可以选择位于下标 2 的字符 'a' 。接着删除下标 2 左侧最近的那个 'a'（位于下标 1）以及下标 2 右侧最近的那个 'a'（位于下标 3）。执行操作后，字符串变为 "da" 。继续对字符串执行任何操作都不会改变其长度。因此，最小化字符串的长度是 2 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> 仅由小写英文字母组成</li>
</ul>
