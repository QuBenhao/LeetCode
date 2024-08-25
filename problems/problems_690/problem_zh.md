# 690. 员工的重要性 

<p>你有一个保存员工信息的数据结构，它包含了员工唯一的 id ，重要度和直系下属的 id 。</p>

<p>给定一个员工数组&nbsp;<code>employees</code>，其中：</p>

<ul>
	<li><code>employees[i].id</code> 是第&nbsp;<code>i</code>&nbsp;个员工的 ID。</li>
	<li><code>employees[i].importance</code>&nbsp;是第&nbsp;<code>i</code>&nbsp;个员工的重要度。</li>
	<li><code>employees[i].subordinates</code> 是第 <code>i</code> 名员工的直接下属的 ID 列表。</li>
</ul>

<p>给定一个整数&nbsp;<code>id</code>&nbsp;表示一个员工的 ID，返回这个员工和他所有下属的重要度的 <strong>总和</strong>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><strong><img alt="" src="https://pic.leetcode.cn/1716170448-dKZffb-image.png" style="width: 400px; height: 258px;" /></strong></p>

<pre>
<strong>输入：</strong>employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]], id = 1
<strong>输出：</strong>11
<strong>解释：</strong>
员工 1 自身的重要度是 5 ，他有两个直系下属 2 和 3 ，而且 2 和 3 的重要度均为 3 。因此员工 1 的总重要度是 5 + 3 + 3 = 11 。
</pre>

<p>&nbsp;</p>

<p><strong>示例 2：</strong></p>

<p><strong><img alt="" src="https://pic.leetcode.cn/1716170929-dkWpra-image.png" style="width: 362px; height: 361px;" /></strong></p>

<pre>
<strong>输入：</strong>employees = [[1,2,[5]],[5,-3,[]]], id = 5
<strong>输出：</strong>-3
<strong>解释：</strong>员工 5 的重要度为 -3 并且没有直接下属。
因此，员工 5 的总重要度为 -3。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= employees.length &lt;= 2000</code></li>
	<li><code>1 &lt;= employees[i].id &lt;= 2000</code></li>
	<li>所有的&nbsp;<code>employees[i].id</code>&nbsp;<strong>互不相同</strong>。</li>
	<li><code>-100 &lt;= employees[i].importance &lt;= 100</code></li>
	<li>一名员工最多有一名直接领导，并可能有多名下属。</li>
	<li><code>employees[i].subordinates</code>&nbsp;中的 ID 都有效。</li>
</ul>
