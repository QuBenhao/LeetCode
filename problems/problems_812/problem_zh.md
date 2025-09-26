# 812. 最大三角形面积 [难度分: 1542.56]

<p>给你一个由 <strong>X-Y</strong> 平面上的点组成的数组 <code>points</code> ，其中 <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> 。从其中取任意三个不同的点组成三角形，返回能组成的最大三角形的面积。与真实值误差在 <code>10<sup>-5</sup></code> 内的答案将会视为正确答案<strong>。</strong></p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/04/1027.png" style="height: 369px; width: 450px;" />
<pre>
<strong>输入：</strong>points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
<strong>输出：</strong>2.00000
<strong>解释：</strong>输入中的 5 个点如上图所示，红色的三角形面积最大。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>points = [[1,0],[0,0],[0,1]]
<strong>输出：</strong>0.50000
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= points.length &lt;= 50</code></li>
	<li><code>-50 &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 50</code></li>
	<li>给出的所有点 <strong>互不相同</strong></li>
</ul>
