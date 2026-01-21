# 853. 车队 [难度分: 1678.11]

<p>在一条单行道上，有 <code>n</code> 辆车开往同一目的地。目的地是几英里以外的&nbsp;<code>target</code>&nbsp;。</p>

<p>给定两个整数数组&nbsp;<code>position</code>&nbsp;和&nbsp;<code>speed</code>&nbsp;，长度都是 <code>n</code> ，其中&nbsp;<code>position[i]</code>&nbsp;是第 <code>i</code> 辆车的位置，&nbsp;<code>speed[i]</code>&nbsp;是第 <code>i</code> 辆车的速度(单位是英里/小时)。</p>

<p>一辆车永远不会超过前面的另一辆车，但它可以追上去，并以较慢车的速度在另一辆车旁边行驶。</p>

<p><strong>车队 </strong>是指并排行驶的一辆或几辆汽车。车队的速度是车队中 <strong>最慢</strong> 的车的速度。</p>

<p>即便一辆车在&nbsp;<code>target</code> 才赶上了一个车队，它们仍然会被视作是同一个车队。</p>

<p>返回到达目的地的车队数量 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]</span></p>

<p><span class="example-io"><b>输出：</b>3</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>从 10（速度为 2）和 8（速度为 4）开始的车会组成一个车队，它们在 12 相遇。车队在&nbsp;<code>target</code>&nbsp;形成。</li>
	<li>从 0（速度为 1）开始的车不会追上其它任何车，所以它自己是一个车队。</li>
	<li>从 5（速度为 1） 和 3（速度为 3）开始的车组成一个车队，在 6 相遇。车队以速度 1 移动直到它到达&nbsp;<code>target</code>。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b></span><span class="example-io">target = 10, position = [3], speed = [3]</span></p>

<p><span class="example-io"><b>输出：</b></span><span class="example-io">1</span></p>

<p><strong>解释：</strong></p>
只有一辆车，因此只有一个车队。</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b></span><span class="example-io">target = 100, position = [0,2,4], speed = [4,2,1]</span></p>

<p><span class="example-io"><b>输出：</b></span><span class="example-io">1</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>从 0（速度为 4） 和 2（速度为 2）开始的车组成一个车队，在 4&nbsp;相遇。从 4 开始的车（速度为 1）移动到了 5。</li>
	<li>然后，在 4（速度为 2）的车队和在 5（速度为 1）的车成为一个车队，在 6 相遇。车队以速度 1 移动直到它到达&nbsp;<code>target</code>。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == position.length == speed.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt; target &lt;= 10<sup>6</sup></code></li>
	<li><code>0 &lt;= position[i] &lt; target</code></li>
	<li><code>position</code>&nbsp;中每个值都 <strong>不同</strong></li>
	<li><code>0 &lt; speed[i] &lt;= 10<sup>6</sup></code></li>
</ul>
