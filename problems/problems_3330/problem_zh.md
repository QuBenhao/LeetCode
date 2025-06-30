# 3330. 找到初始输入字符串 I [难度分: 1338.27]

<p>Alice 正在她的电脑上输入一个字符串。但是她打字技术比较笨拙，她&nbsp;<strong>可能</strong>&nbsp;在一个按键上按太久，导致一个字符被输入&nbsp;<strong>多次</strong>&nbsp;。</p>

<p>尽管 Alice 尽可能集中注意力，她仍然可能会犯错 <strong>至多</strong>&nbsp;一次。</p>

<p>给你一个字符串&nbsp;<code>word</code> ，它表示 <strong>最终</strong>&nbsp;显示在 Alice 显示屏上的结果。</p>

<p>请你返回 Alice 一开始可能想要输入字符串的总方案数。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>word = "abbcccc"</span></p>

<p><span class="example-io"><b>输出：</b>5</span></p>

<p><strong>解释：</strong></p>

<p>可能的字符串包括：<code>"abbcccc"</code>&nbsp;，<code>"abbccc"</code>&nbsp;，<code>"abbcc"</code>&nbsp;，<code>"abbc"</code>&nbsp;和&nbsp;<code>"abcccc"</code>&nbsp;。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>word = "abcd"</span></p>

<p><span class="example-io"><b>输出：</b>1</span></p>

<p><strong>解释：</strong></p>

<p>唯一可能的字符串是&nbsp;<code>"abcd"</code>&nbsp;。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>word = "aaaa"</span></p>

<p><span class="example-io"><b>输出：</b>4</span></p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 100</code></li>
	<li><code>word</code>&nbsp;只包含小写英文字母。</li>
</ul>
