# 874. 模拟行走机器人 [难度分: 1846.36]

<p>机器人在一个无限大小的 XY 网格平面上行走，从点&nbsp;<code>(0, 0)</code> 处开始出发，面向北方。该机器人可以接收以下三种类型的命令 <code>commands</code> ：</p>

<ul>
	<li><code>-2</code> ：向左转&nbsp;<code>90</code> 度</li>
	<li><code>-1</code> ：向右转 <code>90</code> 度</li>
	<li><code>1 &lt;= x &lt;= 9</code> ：向前移动&nbsp;<code>x</code>&nbsp;个单位长度</li>
</ul>

<p>在网格上有一些格子被视为障碍物&nbsp;<code>obstacles</code> 。第 <code>i</code>&nbsp;个障碍物位于网格点 &nbsp;<code>obstacles[i] = (x<sub>i</sub>, y<sub>i</sub>)</code> 。</p>

<p>机器人无法走到障碍物上，它将会停留在障碍物的前一个网格方块上，并继续执行下一个命令。</p>

<p>返回机器人距离原点的 <strong>最大欧式距离</strong> 的 <strong>平方</strong> 。（即，如果距离为 <code>5</code> ，则返回 <code>25</code> ）</p>

<div class="d-google dictRoot saladict-panel isAnimate">
<div>
<div class="MachineTrans-Text">
<div class="MachineTrans-Lines">
<div class="MachineTrans-Lines-collapse MachineTrans-lang-en">&nbsp;</div>
</div>

<div class="MachineTrans-Lines">
<p class="MachineTrans-lang-zh-CN"><strong>注意：</strong></p>

<ul>
	<li class="MachineTrans-lang-zh-CN">北方表示 +Y 方向。</li>
	<li class="MachineTrans-lang-zh-CN">东方表示 +X 方向。</li>
	<li class="MachineTrans-lang-zh-CN">南方表示 -Y 方向。</li>
	<li class="MachineTrans-lang-zh-CN">西方表示 -X 方向。</li>
	<li class="MachineTrans-lang-zh-CN">原点 [0,0] 可能会有障碍物。</li>
</ul>
</div>
</div>
</div>
</div>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>commands = [4,-1,3], obstacles = []
<strong>输出：</strong>25
<strong>解释：
</strong>机器人开始位于 (0, 0)：
1. 向北移动 4 个单位，到达 (0, 4)
2. 右转
3. 向东移动 3 个单位，到达 (3, 4)
距离原点最远的是 (3, 4) ，距离为 3<sup>2</sup> + 4<sup>2</sup> = 25</pre>

<p><strong>示例&nbsp;2：</strong></p>

<pre>
<strong>输入：</strong>commands = [4,-1,4,-2,4], obstacles = [[2,4]]
<strong>输出：</strong>65
<strong>解释</strong>：机器人开始位于 (0, 0)：
1. 向北移动 4 个单位，到达 (0, 4)
2. 右转
3. 向东移动 1 个单位，然后被位于 (2, 4) 的障碍物阻挡，机器人停在 (1, 4)
4. 左转
5. 向北走 4 个单位，到达 (1, 8)
距离原点最远的是 (1, 8) ，距离为 1<sup>2</sup> + 8<sup>2</sup> = 65</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>commands = [6,-1,-1,6], obstacles = []
<b>输出：</b>36
<b>解释：</b>机器人开始位于 (0, 0):
1. 向北移动 6 个单位，到达 (0, 6).
2. 右转
3. 右转
4. 向南移动 6 个单位，到达 (0, 0).
机器人距离原点最远的点是 (0, 6)，其距离的平方是 6<sup>2</sup> = 36 个单位。</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= commands.length &lt;= 10<sup>4</sup></code></li>
	<li><code>commands[i]</code> 的值可以取 <code>-2</code>、<code>-1</code> 或者是范围 <code>[1, 9]</code> 内的一个整数。</li>
	<li><code>0 &lt;= obstacles.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-3 * 10<sup>4</sup> &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 3 * 10<sup>4</sup></code></li>
	<li>答案保证小于 <code>2<sup>31</sup></code></li>
</ul>
