# 909. 蛇梯棋 [难度分: 2019.54]

<p>给你一个大小为 <code>n x n</code> 的整数矩阵 <code>board</code> ，方格按从&nbsp;<code>1</code> 到 <code>n<sup>2</sup></code> 编号，编号遵循 <a href="https://baike.baidu.com/item/%E7%89%9B%E8%80%95%E5%BC%8F%E8%BD%AC%E8%A1%8C%E4%B9%A6%E5%86%99%E6%B3%95/17195786">转行交替方式</a><strong> </strong>，<strong>从左下角开始</strong>&nbsp;（即，从 <code>board[n - 1][0]</code> 开始）的每一行改变方向。</p>

<p>你一开始位于棋盘上的方格&nbsp; <code>1</code>。每一回合，玩家需要从当前方格 <code>curr</code> 开始出发，按下述要求前进：</p>

<ul>
	<li>选定目标方格 <code>next</code> ，目标方格的编号在范围&nbsp;<code>[curr + 1, min(curr + 6, n<sup>2</sup>)]</code> 。
	<ul>
		<li>该选择模拟了掷 <strong>六面体骰子</strong> 的情景，无论棋盘大小如何，玩家最多只能有 6 个目的地。</li>
	</ul>
	</li>
	<li>传送玩家：如果目标方格 <code>next</code> 处存在蛇或梯子，那么玩家会传送到蛇或梯子的目的地。否则，玩家传送到目标方格 <code>next</code> 。&nbsp;</li>
	<li>当玩家到达编号 <code>n<sup>2</sup></code> 的方格时，游戏结束。</li>
</ul>

<p>如果 <code>board[r][c] != -1</code>&nbsp;，位于&nbsp;<code>r</code> 行 <code>c</code> 列的棋盘格中可能存在 “蛇” 或 “梯子”。那个蛇或梯子的目的地将会是 <code>board[r][c]</code>。编号为 <code>1</code> 和 <code>n<sup>2</sup></code> 的方格不是任何蛇或梯子的起点。</p>

<p>注意，玩家在每次掷骰的前进过程中最多只能爬过蛇或梯子一次：就算目的地是另一条蛇或梯子的起点，玩家也 <strong>不能</strong> 继续移动。</p>

<ul>
	<li>举个例子，假设棋盘是 <code>[[-1,4],[-1,3]]</code> ，第一次移动，玩家的目标方格是 <code>2</code> 。那么这个玩家将会顺着梯子到达方格 <code>3</code> ，但 <strong>不能</strong> 顺着方格 <code>3</code> 上的梯子前往方格 <code>4</code> 。（简单来说，类似飞行棋，玩家掷出骰子点数后移动对应格数，遇到单向的路径（即梯子或蛇）可以直接跳到路径的终点，但如果多个路径首尾相连，也不能连续跳多个路径）</li>
</ul>

<p>返回达到编号为&nbsp;<code>n<sup>2</sup></code> 的方格所需的最少掷骰次数，如果不可能，则返回 <code>-1</code>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/09/23/snakes.png" style="width: 500px; height: 394px;" />
<pre>
<strong>输入：</strong>board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
<strong>输出：</strong>4
<strong>解释：</strong>
首先，从方格 1 [第 5 行，第 0 列] 开始。 
先决定移动到方格 2 ，并必须爬过梯子移动到到方格 15 。
然后决定移动到方格 17 [第 3 行，第 4 列]，必须爬过蛇到方格 13 。
接着决定移动到方格 14 ，且必须通过梯子移动到方格 35 。 
最后决定移动到方格 36 , 游戏结束。 
可以证明需要至少 4 次移动才能到达最后一个方格，所以答案是 4 。 
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>board = [[-1,-1],[-1,3]]
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == board.length == board[i].length</code></li>
	<li><code>2 &lt;= n &lt;= 20</code></li>
	<li><code>board[i][j]</code> 的值是 <code>-1</code> 或在范围 <code>[1, n<sup>2</sup>]</code> 内</li>
	<li>编号为 <code>1</code> 和 <code>n<sup>2</sup></code> 的方格上没有蛇或梯子</li>
</ul>
