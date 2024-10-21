# 3184. 构成整天的下标对数目 I [难度分: 1149.55]

<p>给你一个整数数组 <code>hours</code>，表示以 <strong>小时 </strong>为单位的时间，返回一个整数，表示满足 <code>i &lt; j</code> 且 <code>hours[i] + hours[j]</code> 构成 <strong>整天 </strong>的下标对&nbsp;<code>i</code>, <code>j</code> 的数目。</p>

<p><strong>整天 </strong>定义为时间持续时间是 24 小时的 <strong>整数倍 </strong>。</p>

<p>例如，1 天是 24 小时，2 天是 48 小时，3 天是 72 小时，以此类推。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">hours = [12,12,30,24,24]</span></p>

<p><strong>输出：</strong> <span class="example-io">2</span></p>

<p><strong>解释：</strong></p>

<p>构成整天的下标对分别是 <code>(0, 1)</code> 和 <code>(3, 4)</code>。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">hours = [72,48,24,3]</span></p>

<p><strong>输出：</strong> <span class="example-io">3</span></p>

<p><strong>解释：</strong></p>

<p>构成整天的下标对分别是 <code>(0, 1)</code>、<code>(0, 2)</code> 和 <code>(1, 2)</code>。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= hours.length &lt;= 100</code></li>
	<li><code>1 &lt;= hours[i] &lt;= 10<sup>9</sup></code></li>
</ul>
