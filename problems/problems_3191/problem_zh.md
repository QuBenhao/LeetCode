# 3191. 使二进制数组全部等于 1 的最少操作次数 I [难度分: 1311.98]

<p>给你一个二进制数组&nbsp;<code>nums</code>&nbsp;。</p>

<p>你可以对数组执行以下操作 <strong>任意</strong>&nbsp;次（也可以 0 次）：</p>

<ul>
	<li>选择数组中 <strong>任意连续</strong>&nbsp;3 个元素，并将它们 <strong>全部反转</strong>&nbsp;。</li>
</ul>

<p><strong>反转</strong>&nbsp;一个元素指的是将它的值从 0 变 1 ，或者从 1 变 0 。</p>

<p>请你返回将 <code>nums</code>&nbsp;中所有元素变为 1 的 <strong>最少</strong>&nbsp;操作次数。如果无法全部变成 1 ，返回 -1 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [0,1,1,1,0,0]</span></p>

<p><span class="example-io"><b>输出：</b>3</span></p>

<p><strong>解释：</strong><br />
我们可以执行以下操作：</p>

<ul>
	<li>选择下标为 0 ，1 和 2 的元素并反转，得到&nbsp;<code>nums = [<u><strong>1</strong></u>,<u><strong>0</strong></u>,<u><strong>0</strong></u>,1,0,0]</code>&nbsp;。</li>
	<li>选择下标为 1 ，2 和 3 的元素并反转，得到&nbsp;<code>nums = [1,<u><strong>1</strong></u>,<u><strong>1</strong></u>,<strong><u>0</u></strong>,0,0]</code>&nbsp;。</li>
	<li>选择下标为 3 ，4 和 5 的元素并反转，得到&nbsp;<code>nums = [1,1,1,<strong><u>1</u></strong>,<u><strong>1</strong></u>,<u><strong>1</strong></u>]</code>&nbsp;。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [0,1,1,1]</span></p>

<p><span class="example-io"><b>输出：</b>-1</span></p>

<p><strong>解释：</strong><br />
无法将所有元素都变为 1 。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1</code></li>
</ul>
