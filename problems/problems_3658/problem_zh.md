# 3658. 奇数和与偶数和的最大公约数 [难度分: 1220.06]

<p>给你一个整数 <code>n</code>。请你计算以下两个值的&nbsp;<strong>最大公约数</strong>（GCD）：</p>

<ul>
	<li>
	<p><code>sumOdd</code>：最小的&nbsp;<code>n</code> 个正奇数的总和。</p>
	</li>
	<li>
	<p><code>sumEven</code>：最小的&nbsp;<code>n</code> 个正偶数的总和。</p>
	</li>
</ul>

<p>返回 <code>sumOdd</code> 和 <code>sumEven</code> 的 GCD。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">n = 4</span></p>

<p><strong>输出：</strong> <span class="example-io">4</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>前 4 个奇数的总和 <code>sumOdd = 1 + 3 + 5 + 7 = 16</code></li>
	<li>前 4 个偶数的总和 <code>sumEven = 2 + 4 + 6 + 8 = 20</code></li>
</ul>

<p>因此，<code>GCD(sumOdd, sumEven) = GCD(16, 20) = 4</code>。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">n = 5</span></p>

<p><strong>输出：</strong> <span class="example-io">5</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>前 5 个奇数的总和 <code>sumOdd = 1 + 3 + 5 + 7 + 9 = 25</code></li>
	<li>前 5 个偶数的总和 <code>sumEven = 2 + 4 + 6 + 8 + 10 = 30</code></li>
</ul>

<p>因此，<code>GCD(sumOdd, sumEven) = GCD(25, 30) = 5</code>。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
</ul>
