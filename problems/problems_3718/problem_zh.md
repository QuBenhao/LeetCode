# 3718. 缺失的最小倍数 [难度分: 1227.63]

<p>给你一个整数数组 <code>nums</code> 和一个整数 <code>k</code>，请返回从 <code>nums</code> 中<strong>缺失的</strong>、<strong>最小的正整数</strong> <code>k</code> 的<strong>倍数</strong>。</p>

<p><strong>倍数</strong> 指能被 <code>k</code> 整除的任意正整数。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [8,2,3,4,6], k = 2</span></p>

<p><strong>输出：</strong> <span class="example-io">10</span></p>

<p><strong>解释：</strong></p>

<p>当 <code>k = 2</code> 时，其倍数为 2、4、6、8、10、12……，其中在 <code>nums</code> 中缺失的最小倍数是 10。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,4,7,10,15], k = 5</span></p>

<p><strong>输出：</strong> <span class="example-io">5</span></p>

<p><strong>解释：</strong></p>

<p>当 <code>k = 5</code> 时，其倍数为 5、10、15、20……，其中在 <code>nums</code> 中缺失的最小倍数是 5。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
	<li><code>1 &lt;= k &lt;= 100</code></li>
</ul>
