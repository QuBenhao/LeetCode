# 3272. 统计好整数的数目 [难度分: 2382.25]

<p>给你两个 <strong>正</strong>&nbsp;整数&nbsp;<code>n</code> 和&nbsp;<code>k</code>&nbsp;。</p>

<p>如果一个整数&nbsp;<code>x</code>&nbsp;满足以下条件，那么它被称为 <strong>k</strong><strong>&nbsp;回文</strong>&nbsp;整数&nbsp;。</p>

<ul>
	<li><code>x</code>&nbsp;是一个&nbsp;<span data-keyword="palindrome-integer">回文整数 。</span></li>
	<li><code>x</code>&nbsp;能被 <code>k</code>&nbsp;整除。</li>
</ul>

<p>如果一个整数的数位重新排列后能得到一个 <strong>k 回文整数</strong>&nbsp;，那么我们称这个整数为&nbsp;<strong>好 </strong>整数。比方说，<code>k = 2</code>&nbsp;，那么&nbsp;2020 可以重新排列得到 2002 ，2002 是一个 k 回文串，所以 2020 是一个好整数。而 1010 无法重新排列数位得到一个 k 回文整数。</p>

<p>请你返回 <code>n</code>&nbsp;个数位的整数中，有多少个 <strong>好</strong>&nbsp;整数。</p>

<p><b>注意</b>&nbsp;，任何整数在重新排列数位之前或者之后 <strong>都不能</strong> 有前导 0 。比方说 1010 不能重排列得到&nbsp;101 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>n = 3, k = 5</span></p>

<p><span class="example-io"><b>输出：</b>27</span></p>

<p><b>解释：</b></p>

<p>部分好整数如下：</p>

<ul>
	<li>551 ，因为它可以重排列得到 515 。</li>
	<li>525 ，因为它已经是一个 k 回文整数。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>n = 1, k = 4</span></p>

<p><span class="example-io"><b>输出：</b>2</span></p>

<p><strong>解释：</strong></p>

<p>两个好整数分别是 4 和 8 。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>n = 5, k = 6</span></p>

<p><span class="example-io"><b>输出：</b>2468</span></p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10</code></li>
	<li><code>1 &lt;= k &lt;= 9</code></li>
</ul>
