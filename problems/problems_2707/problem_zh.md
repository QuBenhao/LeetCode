# 2707. 字符串中的额外字符 [难度分: 1735.85]

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的字符串&nbsp;<code>s</code>&nbsp;和一个单词字典&nbsp;<code>dictionary</code>&nbsp;。你需要将&nbsp;<code>s</code>&nbsp;分割成若干个 <strong>互不重叠</strong>&nbsp;的子字符串，每个子字符串都在&nbsp;<code>dictionary</code>&nbsp;中出现过。<code>s</code>&nbsp;中可能会有一些&nbsp;<strong>额外的字符</strong>&nbsp;不在任何子字符串中。</p>

<p>请你采取最优策略分割 <code>s</code>&nbsp;，使剩下的字符 <strong>最少</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>s = "leetscode", dictionary = ["leet","code","leetcode"]
<b>输出：</b>1
<b>解释：</b>将 s 分成两个子字符串：下标从 0 到 3 的 "leet" 和下标从 5 到 8 的 "code" 。只有 1 个字符没有使用（下标为 4），所以我们返回 1 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>s = "sayhelloworld", dictionary = ["hello","world"]
<b>输出：</b>3
<b>解释：</b>将 s 分成两个子字符串：下标从 3 到 7 的 "hello" 和下标从 8 到 12 的 "world" 。下标为 0 ，1 和 2 的字符没有使用，所以我们返回 3 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 50</code></li>
	<li><code>1 &lt;= dictionary.length &lt;= 50</code></li>
	<li><code>1 &lt;= dictionary[i].length &lt;= 50</code></li>
	<li><code>dictionary[i]</code>&nbsp;和&nbsp;<code>s</code>&nbsp;只包含小写英文字母。</li>
	<li><code>dictionary</code>&nbsp;中的单词互不相同。</li>
</ul>
