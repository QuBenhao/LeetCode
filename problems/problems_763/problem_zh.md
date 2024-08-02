# 763. 划分字母区间 [难度分: 1443.07]

<p>给你一个字符串 <code>s</code> 。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。</p>

<p>注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是 <code>s</code> 。</p>

<p>返回一个表示每个字符串片段的长度的列表。</p>

<p>&nbsp;</p>
<strong class="example">示例 1：</strong>

<pre>
<strong>输入：</strong>s = "ababcbacadefegdehijhklij"
<strong>输出：</strong>[9,7,8]
<strong>解释：</strong>
划分结果为 "ababcbaca"、"defegde"、"hijhklij" 。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 这样的划分是错误的，因为划分的片段数较少。 </pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "eccbbbbdec"
<strong>输出：</strong>[10]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 500</code></li>
	<li><code>s</code> 仅由小写英文字母组成</li>
</ul>
