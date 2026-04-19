# 2078. 两栋颜色不同且距离最远的房子 [难度分: 1240.83]

<p>街上有 <code>n</code> 栋房子整齐地排成一列，每栋房子都粉刷上了漂亮的颜色。给你一个下标从 <strong>0</strong> 开始且长度为 <code>n</code> 的整数数组 <code>colors</code> ，其中 <code>colors[i]</code> 表示第&nbsp; <code>i</code> 栋房子的颜色。</p>

<p>返回 <strong>两栋</strong> 颜色 <strong>不同</strong> 房子之间的 <strong>最大</strong> 距离。</p>

<p>第 <code>i</code> 栋房子和第 <code>j</code> 栋房子之间的距离是 <code>abs(i - j)</code> ，其中 <code>abs(x)</code> 是 <code>x</code> 的绝对值。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/10/31/eg1.png" style="width: 610px; height: 84px;" /></p>

<pre>
<strong>输入：</strong>colors = [<strong><em>1</em></strong>,1,1,<em><strong>6</strong></em>,1,1,1]
<strong>输出：</strong>3
<strong>解释：</strong>上图中，颜色 1 标识成蓝色，颜色 6 标识成红色。
两栋颜色不同且距离最远的房子是房子 0 和房子 3 。
房子 0 的颜色是颜色 1 ，房子 3 的颜色是颜色 6 。两栋房子之间的距离是 abs(0 - 3) = 3 。
注意，房子 3 和房子 6 也可以产生最佳答案。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/10/31/eg2.png" style="width: 426px; height: 84px;" /></p>

<pre>
<strong>输入：</strong>colors = [<em><strong>1</strong></em>,8,3,8,<em><strong>3</strong></em>]
<strong>输出：</strong>4
<strong>解释：</strong>上图中，颜色 1 标识成蓝色，颜色 8 标识成黄色，颜色 3 标识成绿色。
两栋颜色不同且距离最远的房子是房子 0 和房子 4 。
房子 0 的颜色是颜色 1 ，房子 4 的颜色是颜色 3 。两栋房子之间的距离是 abs(0 - 4) = 4 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>colors = [<em><strong>0</strong></em>,<em><strong>1</strong></em>]
<strong>输出：</strong>1
<strong>解释：</strong>两栋颜色不同且距离最远的房子是房子 0 和房子 1 。
房子 0 的颜色是颜色 0 ，房子 1 的颜色是颜色 1 。两栋房子之间的距离是 abs(0 - 1) = 1 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n ==&nbsp;colors.length</code></li>
	<li><code>2 &lt;= n &lt;= 100</code></li>
	<li><code>0 &lt;= colors[i] &lt;= 100</code></li>
	<li>生成的测试数据满足 <strong>至少 </strong>存在 2 栋颜色不同的房子</li>
</ul>
