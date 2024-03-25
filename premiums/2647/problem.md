# 2647. Color the Triangle Red

<p>You are given an integer <code>n</code>. Consider an equilateral triangle of side length <code>n</code>, broken up into <code>n<sup>2</sup></code> unit equilateral triangles. The triangle has <code>n</code> <strong>1-indexed</strong> rows where the <code>i<sup>th</sup></code> row has <code>2i - 1</code> unit equilateral triangles.</p>

<p>The triangles in the <code>i<sup>th</sup></code> row are also <strong>1-indexed</strong> with coordinates from <code>(i, 1)</code> to <code>(i, 2i - 1)</code>. The following image shows a triangle of side length <code>4</code> with the indexing of its triangle.</p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/09/01/triangle4.jpg" style="width: 402px; height: 242px;" />
<p>Two triangles are <strong>neighbors</strong> if they <strong>share a side</strong>. For example:</p>

<ul>
	<li>Triangles <code>(1,1)</code> and <code>(2,2)</code> are neighbors</li>
	<li>Triangles <code>(3,2)</code> and <code>(3,3)</code> are neighbors.</li>
	<li>Triangles <code>(2,2)</code> and <code>(3,3)</code> are not neighbors because they do not share any side.</li>
</ul>

<p>Initially, all the unit triangles are <strong>white</strong>. You want to choose <code>k</code> triangles and color them <strong>red</strong>. We will then run the following algorithm:</p>

<ol>
	<li>Choose a white triangle that has <strong>at least two</strong> red neighbors.

	<ul>
		<li>If there is no such triangle, stop the algorithm.</li>
	</ul>
	</li>
	<li>Color that triangle <strong>red</strong>.</li>
	<li>Go to step 1.</li>
</ol>

<p>Choose the minimum <code>k</code> possible and set <code>k</code> triangles red before running this algorithm such that after the algorithm stops, all unit triangles are colored red.</p>

<p>Return <em>a 2D list of the coordinates of the triangles that you will color red initially</em>. The answer has to be of the smallest size possible. If there are multiple valid solutions, return any.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/09/01/example1.jpg" style="width: 500px; height: 263px;" />
<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> [[1,1],[2,1],[2,3],[3,1],[3,5]]
<strong>Explanation:</strong> Initially, we choose the shown 5 triangles to be red. Then, we run the algorithm:
- Choose (2,2) that has three red neighbors and color it red.
- Choose (3,2) that has two red neighbors and color it red.
- Choose (3,4) that has three red neighbors and color it red.
- Choose (3,3) that has three red neighbors and color it red.
It can be shown that choosing any 4 triangles and running the algorithm will not make all triangles red.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/09/01/example2.jpg" style="width: 300px; height: 101px;" />
<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> [[1,1],[2,1],[2,3]]
<strong>Explanation:</strong> Initially, we choose the shown 3 triangles to be red. Then, we run the algorithm:
- Choose (2,2) that has three red neighbors and color it red.
It can be shown that choosing any 2 triangles and running the algorithm will not make all triangles red.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
</ul>
