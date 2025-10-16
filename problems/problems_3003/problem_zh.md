# 3003. 执行操作后的最大分割数量 [难度分: 3039.30]

<p>给你一个下标从 <strong>0</strong> 开始的字符串&nbsp;<code>s</code>&nbsp;和一个整数&nbsp;<code>k</code>。</p>

<p>你需要执行以下分割操作，直到字符串&nbsp;<code>s&nbsp;</code>变为&nbsp;<strong>空</strong>：</p>

<ul>
	<li>选择&nbsp;<code>s</code>&nbsp;的最长&nbsp;<strong>前缀</strong>，该前缀最多包含&nbsp;<code>k&nbsp;</code>个&nbsp;<strong>不同&nbsp;</strong>字符。</li>
	<li><strong>删除&nbsp;</strong>这个前缀，并将分割数量加一。如果有剩余字符，它们在&nbsp;<code>s</code>&nbsp;中保持原来的顺序。</li>
</ul>

<p>执行操作之 <strong>前</strong> ，你可以将&nbsp;<code>s</code>&nbsp;中&nbsp;<strong>至多一处 </strong>下标的对应字符更改为另一个小写英文字母。</p>

<p>在最优选择情形下改变至多一处下标对应字符后，用整数表示并返回操作结束时得到的 <strong>最大</strong> 分割数量。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">s = "accca", k = 2</span></p>

<p><strong>输出：</strong><span class="example-io">3</span></p>

<p><strong>解释：</strong></p>

<p>最好的方式是把&nbsp;<code>s[2]</code>&nbsp;变为除了 a 和 c 之外的东西，比如&nbsp;b。然后它变成了&nbsp;<code>"acbca"</code>。</p>

<p>然后我们执行以下操作：</p>

<ol>
	<li>最多包含 2 个不同字符的最长前缀是 <code>"ac"</code>，我们删除它然后&nbsp;<code>s</code> 变为&nbsp;<code>"bca"</code>。</li>
	<li>现在最多包含 2 个不同字符的最长前缀是&nbsp;<code>"bc"</code>，所以我们删除它然后&nbsp;<code>s</code> 变为&nbsp;<code>"a"</code>。</li>
	<li>最后，我们删除&nbsp;<code>"a"</code>&nbsp;并且&nbsp;<code>s</code>&nbsp;变成空串，所以该过程结束。</li>
</ol>

<p>进行操作时，字符串被分成 3 个部分，所以答案是 3。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">s = "aabaab", k = 3</span></p>

<p><strong>输出：</strong><span class="example-io">1</span></p>

<p><strong>解释：</strong></p>

<p>一开始&nbsp;<code>s</code>&nbsp;包含 2 个不同的字符，所以无论我们改变哪个，&nbsp;它最多包含 3 个不同字符，因此最多包含 3 个不同字符的最长前缀始终是所有字符，因此答案是 1。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">s = "xxyz", k = 1</span></p>

<p><span class="example-io"><b>输出：</b>4</span></p>

<p><strong>解释：</strong></p>

<p>最好的方式是将&nbsp;<code>s[0]</code>&nbsp;或&nbsp;<code>s[1]</code>&nbsp;变为&nbsp;<code>s</code>&nbsp;中字符以外的东西，例如将&nbsp;<code>s[0]</code>&nbsp;变为&nbsp;<code>w</code>。</p>

<p>然后&nbsp;<code>s</code>&nbsp;变为&nbsp;<code>"wxyz"</code>，包含 4 个不同的字符，所以当&nbsp;<code>k</code>&nbsp;为 1，它将分为 4 个部分。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code>&nbsp;只包含小写英文字母。</li>
	<li><code>1 &lt;= k &lt;= 26</code></li>
</ul>
