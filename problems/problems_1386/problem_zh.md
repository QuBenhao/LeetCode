# 1386. 安排电影院座位 [难度分: 1636.69]

<p><img alt="" src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/03/21/cinema_seats_1.png" style="height: 149px; width: 400px;" /></p>

<p>如上图所示，电影院的观影厅中有 <code>n</code>&nbsp;行座位，行编号从 1&nbsp;到 <code>n</code>&nbsp;，且每一行内总共有 10 个座位，列编号从 1 到 10 。</p>

<p>给定一个二维数组&nbsp;<code>reservedSeats</code>&nbsp;，其中&nbsp;<code>reservedSeats[i] = [row<sub>i</sub>, seat<sub>i</sub>]</code> 表示第&nbsp;<code>row<sub>i</sub></code> 行的座位&nbsp;<code>seat<sub>i</sub></code> 已经被预定。</p>

<p>四人小组必须被安排在同一排的四个座位上。该小组可以坐在以下座位块之一：</p>

<ul>
	<li>座位 <code>2, 3, 4, 5</code></li>
	<li>座位 <code>4, 5, 6, 7</code></li>
	<li>座位 <code>6, 7, 8, 9</code></li>
</ul>

<p>只有当该块中的所有座位都 <strong>没有</strong> 被预订时，才能使用该块。每个座位 <strong>最多</strong> 只能分配给一个小组。</p>

<p>返回一个整数，表示可以分配的 <strong>最大</strong> 四人小组数量。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/03/21/cinema_seats_3.png" style="height: 96px; width: 400px;" /></p>

<pre>
<strong>输入：</strong>n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
<strong>输出：</strong>4
<strong>解释：</strong>上图所示是最优的安排方案，总共可以安排 4 个家庭。蓝色的叉表示被预约的座位，橙色的连续座位表示一个 4 人家庭。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 2, reservedSeats = [[2,1],[1,8],[2,6]]
<strong>输出：</strong>2
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
<strong>输出：</strong>4
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;=&nbsp;reservedSeats.length &lt;= min(10 * n, 10<sup>4</sup>)</code></li>
	<li><code>reservedSeats[i]&nbsp;== [row<sub>i</sub>, seat<sub>i</sub>]</code></li>
	<li><code>1&nbsp;&lt;=&nbsp;row<sub>i</sub> &lt;= n</code></li>
	<li><code>1 &lt;=&nbsp;seat<sub>i</sub> &lt;= 10</code></li>
	<li>所有&nbsp;<code>reservedSeats[i]</code> 都是互不相同的。</li>
</ul>
