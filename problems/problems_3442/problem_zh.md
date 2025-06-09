# 3442. 奇偶频次间的最大差值 I [难度分: 1220.14]

<p>给你一个由小写英文字母组成的字符串&nbsp;<code>s</code> 。</p>

<p>请你找出字符串中两个字符&nbsp;<code>a<sub>1</sub></code>&nbsp;和&nbsp;<code>a<sub>2</sub></code> 的出现频次之间的 <strong>最大</strong> 差值 <code>diff = a<sub>1</sub>&nbsp;- a<sub>2</sub></code>，这两个字符需要满足：</p>

<ul>
	<li><code>a<sub>1</sub></code>&nbsp;在字符串中出现 <strong>奇数次</strong> 。</li>
	<li><code>a<sub>2</sub></code>&nbsp;在字符串中出现 <strong>偶数次</strong>&nbsp;。</li>
</ul>

<p>返回 <strong>最大</strong> 差值。</p>

<p>&nbsp;</p>

<p><b>示例 1：</b></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>s = "aaaaabbc"</span></p>

<p><b>输出：</b>3</p>

<p><b>解释：</b></p>

<ul>
	<li>字符&nbsp;<code>'a'</code>&nbsp;出现 <strong>奇数次</strong>&nbsp;，次数为&nbsp;<code><font face="monospace">5</font></code><font face="monospace"> ；字符</font>&nbsp;<code>'b'</code>&nbsp;出现 <strong>偶数次</strong> ，次数为&nbsp;<code><font face="monospace">2</font></code>&nbsp;。</li>
	<li>最大差值为&nbsp;<code>5 - 2 = 3</code>&nbsp;。</li>
</ul>
</div>

<p><b>示例 2：</b></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>s = "abcabcab"</span></p>

<p><b>输出：</b>1</p>

<p><b>解释：</b></p>

<ul>
	<li>字符&nbsp;<code>'a'</code>&nbsp;出现 <strong>奇数次</strong>&nbsp;，次数为&nbsp;<code><font face="monospace">3</font></code><font face="monospace"> ；字符</font>&nbsp;<code>'c'</code>&nbsp;出现 <strong>偶数次</strong>&nbsp;，次数为&nbsp;<font face="monospace">2 。</font></li>
	<li>最大差值为&nbsp;<code>3 - 2 = 1</code> 。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><b>提示：</b></p>

<ul>
	<li><code>3 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code>&nbsp;仅由小写英文字母组成。</li>
	<li><code>s</code>&nbsp;至少由一个出现奇数次的字符和一个出现偶数次的字符组成。</li>
</ul>
