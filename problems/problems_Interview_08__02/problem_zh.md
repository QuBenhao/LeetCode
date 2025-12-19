# 面试题 08.02. 迷路的机器人 

<p>设想有个机器人坐在一个网格的左上角，网格 r 行 c 列。机器人只能向下或向右移动，但不能走到一些被禁止的网格（有障碍物）。设计一种算法，寻找机器人从左上角移动到右下角的路径。</p>

<p><img src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/10/22/robot_maze.png" style="height: 183px; width: 400px;" /></p>

<p>网格中的障碍物和空位置分别用 <code>1</code> 和 <code>0</code> 来表示。</p>

<p>返回一条可行的路径，路径由经过的网格的行号和列号组成。左上角为 0 行 0 列。如果没有可行的路径，返回空数组。</p>

<p><strong>示例&nbsp;1：</strong></p>

<pre>
<strong>输入：</strong>[[0,0,0],[0,1,0],[0,0,0]]
<strong>输出：</strong>[[0,0],[0,1],[0,2],[1,2],[2,2]]
<strong>解释：
</strong>输入中标粗的位置即为输出表示的路径，即
0 行 0 列（左上角） -&gt; 0 行 1 列 -&gt; 0 行 2 列 -&gt; 1 行 2 列 -&gt; 2 行 2 列（右下角）</pre>

<p><strong>说明：</strong><em>r</em>&nbsp;和 <em>c </em>的值均不超过 100。</p>
