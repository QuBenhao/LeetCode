# 1792. 最大平均通过率 [难度分: 1818.00]

<p>一所学校里有一些班级，每个班级里有一些学生，现在每个班都会进行一场期末考试。给你一个二维数组 <code>classes</code> ，其中 <code>classes[i] = [pass<sub>i</sub>, total<sub>i</sub>]</code> ，表示你提前知道了第 <code>i</code> 个班级总共有 <code>total<sub>i</sub></code> 个学生，其中只有 <code>pass<sub>i</sub></code> 个学生可以通过考试。</p>

<p>给你一个整数 <code>extraStudents</code> ，表示额外有 <code>extraStudents</code> 个聪明的学生，他们 <strong>一定</strong> 能通过任何班级的期末考。你需要给这 <code>extraStudents</code> 个学生每人都安排一个班级，使得 <strong>所有</strong> 班级的 <strong>平均</strong> 通过率 <strong>最大</strong> 。</p>

<p>一个班级的 <strong>通过率</strong> 等于这个班级通过考试的学生人数除以这个班级的总人数。<strong>平均通过率</strong> 是所有班级的通过率之和除以班级数目。</p>

<p>请你返回在安排这 <code><span style="">extraStudents</span></code> 个学生去对应班级后的 <strong>最大</strong> 平均通过率。与标准答案误差范围在 <code>10<sup>-5</sup></code> 以内的结果都会视为正确结果。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>classes = [[1,2],[3,5],[2,2]], <code>extraStudents</code> = 2
<b>输出：</b>0.78333
<b>解释：</b>你可以将额外的两个学生都安排到第一个班级，平均通过率为 (3/4 + 3/5 + 2/2) / 3 = 0.78333 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>classes = [[2,4],[3,9],[4,5],[2,10]], <code>extraStudents</code> = 4
<strong>输出：</strong>0.53485
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= classes.length <= 10<sup>5</sup></code></li>
	<li><code>classes[i].length == 2</code></li>
	<li><code>1 <= pass<sub>i</sub> <= total<sub>i</sub> <= 10<sup>5</sup></code></li>
	<li><code>1 <= extraStudents <= 10<sup>5</sup></code></li>
</ul>
