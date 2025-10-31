# 3217. 从链表中移除在数组中存在的节点 [难度分: 1341.72]

<p>给你一个整数数组 <code>nums</code> 和一个链表的头节点 <code>head</code>。从链表中<strong>移除</strong>所有存在于 <code>nums</code> 中的节点后，返回修改后的链表的头节点。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,2,3], head = [1,2,3,4,5]</span></p>

<p><strong>输出：</strong> <span class="example-io">[4,5]</span></p>

<p><strong>解释：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2024/06/11/linkedlistexample0.png" style="width: 400px; height: 66px;" /></strong></p>

<p>移除数值为 1, 2 和 3 的节点。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1], head = [1,2,1,2,1,2]</span></p>

<p><strong>输出：</strong> <span class="example-io">[2,2,2]</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/06/11/linkedlistexample1.png" style="height: 62px; width: 450px;" /></p>

<p>移除数值为 1 的节点。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [5], head = [1,2,3,4]</span></p>

<p><strong>输出：</strong> <span class="example-io">[1,2,3,4]</span></p>

<p><strong>解释：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2024/06/11/linkedlistexample2.png" style="width: 400px; height: 83px;" /></strong></p>

<p>链表中不存在值为 5 的节点。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>nums</code> 中的所有元素都是唯一的。</li>
	<li>链表中的节点数在 <code>[1, 10<sup>5</sup>]</code> 的范围内。</li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
	<li>输入保证链表中至少有一个值没有在&nbsp;<code>nums</code> 中出现过。</li>
</ul>
