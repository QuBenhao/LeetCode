# LeetCode
Algorithms in LeetCode by Benhao

# How to start
After clone this repo, add a .env file to tell where to locate your problems and solutions (locally).
For remote GitHub Action, add `COOKIE` (LeetCode cookie), `PUSH_KEY` (PushDeer notification), `PROBLEM_FOLDER` (where to add problems), `USER` (LeetCode personal page uri).

Example .env file:
```text
PROBLEM_FOLDER="problems"
PUSH_KEY="***[key from PushDeer]"
COOKIE="***[cookie from LeetCode graphql]"
```

install requirements:
```shell
pip install -r requirements
```

And then, **change QUESTION id in [test.py](./test.py)**, and try:
```shell
python3 ./test.py
```

# Table of Content
1. [Easy](#easy)
2. [Medium](#medium) 
3. [Hard](#hard)
4. [Mysql](#mysql)
5. [LCP](#lcp)
6. [面试题](#interview)

# Problems

## Easy

[1480.Running Sum of 1d Array](problems/1480/problem.md)

[1431.Kids With the Greatest Number of Candies](problems/1431/problem.md)

[1470.Shuffle the Array](problems/1470/problem.md)

[1512.Number of Good Pairs](problems/1512/problem.md)

[1108.Defanging an IP Address](problems/1108/problem.md)

[771.Jewels and Stones](problems/771/problem.md)

[665.Non-decreasing Array](problems/665/problem.md)

[1342.Number of Steps to Reduce a Number to Zero](problems/1342/problem.md)

[1528.Shuffle String](problems/1528/problem.md)

[1365.How Many Numbers Are Smaller Than the Current Number](problems/1365/problem.md)

[1281.Subtract the Product and Sum of Digits of an Integer](problems/1281/problem.md)

[1603.Design Parking System](problems/1603/problem.md)

[1313.Decompress Run-Length Encoded List](problems/1313/problem.md)

[1614.Maximum Nesting Depth of the Parentheses](problems/1614/problem.md)

[1389.Create Target Array in the Given Order](problems/1389/problem.md)

[1486.XOR Operation in an Array](problems/1486/problem.md)

[1221.Split a String in Balanced Strings](problems/1221/problem.md)

[1662.Check If Two String Arrays are Equivalent](problems/1662/problem.md)

[66.Plus One](problems/66/problem.md)

[1672.Richest Customer Wealth](problems/1672/problem.md)

[938.Range Sum of BST](problems/938/problem.md)

[1290.Convert Binary Number in a Linked List to Integer](problems/1290/problem.md)

[1588.Sum of All Odd Length Subarrays](problems/1588/problem.md)

[1656.Design an Ordered Stream](problems/1656/problem.md)

[104.Maximum Depth of Binary Tree Solution](problems/104/problem.md)

[83.Remove Duplicates from Sorted List](problems/83/problem.md)

[897.Increasing Order Search Tree](problems/897/problem.md)

[605.Can Place Flowers](problems/605/problem.md)

[1678.Goal Parser Interpretation](problems/1678/problem.md)

[941.Valid Mountain Array](problems/941/problem.md)

[944.Delete Columns to Make Sorted](problems/944/problem.md)

[812.Largest Triangle Area](problems/812/problem.md)

[26.Remove Duplicates from Sorted Array](problems/26/problem.md)

[190.Reverse Bits](problems/190/problem.md)

[1.Two Sum](problems/1/problem.md)

[1684.Count the Number of Consistent Strings](problems/1684/problem.md)

[1688.Count of Matches in Tournament](problems/1688/problem.md)

[53.Maximum Subarray](problems/53/problem.md)

[977.Squares of a Sorted Array](problems/977/problem.md)

[136.Single Number](problems/136/problem.md)

[1694.Reformat Phone Number](problems/1694/problem.md)

[908.Smallest Range I](problems/908/problem.md)

[141.Linked List Cycle](problems/141/problem.md)

[110.Balanced Binary Tree](problems/110/problem.md)

[1030.Matrix Cells in Distance Order](problems/1030/problem.md)

[496.Next Greater Element I](problems/496/problem.md)

[1700.Number of Students Unable to Eat Lunch](problems/1700/problem.md)

[1704.Determine if String Halves Are Alike](problems/1704/problem.md)

[121.Best Time to Buy and Sell Stock](problems/121/problem.md)

[122.Best Time to Buy and Sell Stock II](problems/122/problem.md)

[733.Flood Fill](problems/733/problem.md)

[1640.Check Array Formation Through Concatenation](problems/1640/problem.md)

[1710.Maximum Units on a Truck](problems/1710/problem.md)

[21.Merge Two Sorted Lists](problems/21/problem.md)

[830.Positions of Large Groups](problems/830/problem.md)

[1539.Kth Missing Positive Number](problems/1539/problem.md)

[1716.Calculate Money in Leetcode Bank](problems/1716/problem.md)

[1720.Decode XORed Array](problems/1720/problem.md)

[88.Merge Sorted Array](problems/88/problem.md)

[1646.Get Maximum in Generated Array](problems/1646/problem.md)

[1725.Number Of Rectangles That Can Form The Largest Square](problems/1725/problem.md)

[20.Valid Parentheses](problems/20/problem.md)

[1732.Find the Highest Altitude](problems/1732/problem.md)

[1736.Latest Time by Replacing Hidden Digits](problems/1736/problem.md)

[23.Merge k Sorted Lists](problems/23/problem.md)

[1437.Check If All 1's Are at Least Length K Places Away](problems/1437/problem.md)

[1742.Maximum Number of Balls in a Box](problems/1742/problem.md)

[191.Number of 1 Bits](problems/191/problem.md)

[594.Longest Harmonious Subsequence](problems/594/problem.md)

[1748.Sum of Unique Elements](problems/1748/problem.md)

[1752.Check if Array Is Sorted and Rotated](problems/1752/problem.md)

[821.Shortest Distance to a Character](problems/821/problem.md)

[242.Valid Anagram](problems/242/problem.md)

[1758.Minimum Changes To Make Alternating Binary String](problems/1758/problem.md)

[1337.The K Weakest Rows in a Matrix](problems/1337/problem.md)

[13.Roman to Integer](problems/13/problem.md)

[1763.Longest Nice Substring](problems/1763/problem.md)

[1768.Merge Strings Alternately](problems/1768/problem.md)

[1773.Count Items Matching a Rule](problems/1773/problem.md)

[303.Range Sum Query - Immutable](problems/303/problem.md)

[232.Implement Queue using Stacks](problems/232/problem.md)

[1779.Find Nearest Point That Has the Same X or Y Coordinate](problems/1779/problem.md)

[1784.Check if Binary String Has at Most One Segment of Ones](problems/1784/problem.md)

[706.Design HashMap](problems/706/problem.md)

[1047.Remove All Adjacent Duplicates In String](problems/1047/problem.md)

[224.Basic Calculator](problems/224/problem.md)

[705.Design HashSet](problems/705/problem.md)

[1790.Check if One String Swap Can Make Strings Equal](problems/1790/problem.md)

[1796.Second Largest Digit in a String](problems/1796/problem.md)

[1800.Maximum Ascending Subarray Sum](problems/1800/problem.md)

[1805.Number of Different Integers in a String](problems/1805/problem.md)

[1812.Determine Color of a Chessboard Square](problems/1812/problem.md)

[1816.Truncate Sentence](problems/1816/problem.md)

[263.Ugly Number](problems/263/problem.md)

[1822.Sign of the Product of an Array](problems/1822/problem.md)

[783.Minimum Distance Between BST Nodes](problems/783/problem.md)

[530.Minimum Absolute Difference in BST](problems/530/problem.md)

[1827.Minimum Operations to Make the Array Increasing](problems/1827/problem.md)

[1832.Check if the Sentence Is Pangram](problems/1832/problem.md)

[27.Remove Element](problems/27/problem.md)

[28.Implement strStr()](problems/28/problem.md)

[204.Count Primes](problems/204/problem.md)

[1837.Sum of Digits in Base K](problems/1837/problem.md)

[690.Employee Importance](problems/690/problem.md)

[1844.Replace All Digits with Characters](problems/1844/problem.md)

[1848.Minimum Distance to the Target Element](problems/1848/problem.md)

[7.Reverse Integer](problems/7/problem.md)

[1854.Maximum Population Year](problems/1854/problem.md)

[872.Leaf-Similar Trees](problems/872/problem.md)

[1859.Sorting the Sentence](problems/1859/problem.md)

[1863.Sum of All Subset XOR Totals](problems/1863/problem.md)

[993.Cousins in Binary Tree](problems/993/problem.md)

[1869.Longer Contiguous Segments of Ones than Zeros](problems/1869/problem.md)

[1668.Maximum Repeating Substring](problems/1668/problem.md)

[461.Hamming Distance](problems/461/problem.md)

[1876.Substrings of Size Three with Distinct Characters](problems/1876/problem.md)

[231.Power of Two](problems/231/problem.md)

[1880.Check if Word Equals Summation of Two Words](problems/1880/problem.md)

[342.Power of Four](problems/342/problem.md)

[1652.Defuse the Bomb](problems/1652/problem.md)

[160.Intersection of Two Linked Lists](problems/160/problem.md)

[203.Remove Linked List Elements](problems/203/problem.md)

[1886.Determine Whether Matrix Can Be Obtained By Rotation](problems/1886/problem.md)

[1893.Check if All the Integers in a Range Are Covered](problems/1893/problem.md)

[1897.Redistribute Characters to Make All Strings Equal](problems/1897/problem.md)

[278.First Bad Version](problems/278/problem.md)

[374.Guess Number Higher or Lower](problems/374/problem.md)

[852.Peak Index in a Mountain Array](problems/852/problem.md)

[1903.Largest Odd Number in String](problems/1903/problem.md)

[401.Binary Watch](problems/401/problem.md)

[1909.Remove One Element to Make the Array Strictly Increasing](problems/1909/problem.md)

[1913.Maximum Product Difference Between Two Pairs](problems/1913/problem.md)

[168.Excel Sheet Column Title](problems/168/problem.md)

[645.Set Mismatch](problems/645/problem.md)

[1920.Build Array from Permutation](problems/1920/problem.md)

[225.Implement Stack using Queues](problems/225/problem.md)

[1925.Count Square Sum Triples](problems/1925/problem.md)

[1929.Concatenation of Array](problems/1929/problem.md)

[155.Min Stack](problems/155/problem.md)

[1935.Maximum Number of Words You Can Type](problems/1935/problem.md)

[1941.Check if All Characters Have Equal Number of Occurrences](problems/1941/problem.md)

[1945.Sum of Digits of String After Convert](problems/1945/problem.md)

[671.Second Minimum Node In a Binary Tree](problems/671/problem.md)

[171.Excel Sheet Column Number](problems/171/problem.md)

[1952.Three Divisors](problems/1952/problem.md)

[1957.Delete Characters to Make Fancy String](problems/1957/problem.md)

[1137.N-th Tribonacci Number](problems/1137/problem.md)

[1961.Check If String Is a Prefix of Array](problems/1961/problem.md)

[1967.Number of Strings That Appear as Substrings in Word](problems/1967/problem.md)

[551.Student Attendance Record I](problems/551/problems.md)

[345.Reverse Vowels of a String](problems/345/problem.md)

[541.Reverse String II](problems/541/problem.md)

## Medium

[2.Add Two Numbers](problems/2/problem.md)

[1476.Subrectangle Queries](problems/1476/problem.md)

[646.Maximum Length of Pair Chain](problems/646/problem.md)

[822.Card Flipping Game](problems/822/problem.md)

[165.Compare Version Numbers](problems/165/problem.md)

[382.Linked List Random Node](problems/382/problem.md)

[1492.The kth Factor of n](problems/1492/problem.md)

[1680.Concatenation of Consecutive Binary Numbers](problems/1680/problem.md)

[1679.Max Number of K-Sum Pairs](problems/1679/problem.md)

[117.Populating Next Right Pointers in Each Node II](problems/117/problem.md)

[59.Spiral Matrix II](problems/59/problem.md)

[1010.Pairs of Songs With Total Durations Divisible by 60](problems/1010/problem.md)

[592.Fraction Addition and Subtraction](problems/592/problem.md)

[801.Minimum Swaps To Make Sequences Increasing](problems/801/problem.md)

[173.Binary Search Tree Iterator](problems/173/problem.md)

[406.Queue Reconstruction by Height](problems/406/problem.md)

[764.Largest Plus Sign](problems/764/problem.md)

[80.Remove Duplicates from Sorted Array II](problems/80/problem.md)

[1382.Balance a Binary Search Tree](problems/1382/problem.md)

[865.Smallest Subtree with all the Deepest Nodes](problems/865/problem.md)

[19.Remove Nth Node From End of List](problems/19/problem.md)

[1685.Sum of Absolute Differences in a Sorted Array](problems/1685/problem.md)

[1686.Stone Game VI](problems/1686/problem.md)

[1689.Partitioning Into Minimum Number Of Deci-Binary Numbers](problems/1689/problem.md)

[1690.Stone Game VII](problems/1690/problem.md)

[131.Palindrome Partitioning](problems/131/problem.md)

[29.Divide Two Integers](problems/29/problem.md)

[954.Array of Doubled Pairs](problems/954/problem.md)

[98.Validate Binary Search Tree](problems/98/problem.md)

[454.4Sum II](problems/454/problem.md)

[18.4Sum](problems/18/problem.md)

[15.3Sum](problems/15/problem.md)

[16.3Sum Closest](problems/16/problem.md)

[36.Valid Sudoku](problems/36/problem.md)

[116.Populating Next Right Pointers in Each Node](problems/116/problem.md)

[334.Increasing Triplet Subsequence](problems/334/problem.md)

[1124.Longest Well-Performing Interval](problems/1124/problem.md)

[962.Maximum Width Ramp](problems/962/problem.md)

[137.Single Number II](problems/137/problem.md)

[1695.Maximum Erasure Value](problems/1695/problem.md)

[1696.Jump Game VI](problems/1696/problem.md)

[880.Decoded String at Index](problems/880/problem.md)

[910.Smallest Range II](problems/910/problem.md)

[556.Next Greater Element III](problems/556/problem.md)

[503.Next Greater Element II](problems/503/problem.md)

[24.Swap Nodes in Pairs](problems/24/problem.md)

[498.Diagonal Traverse](problems/498/problem.md)

[1424.Diagonal Traverse II](problems/1424/problem.md)

[144.Binary Tree Preorder Traversal](problems/144/problem.md)

[91.Decode Ways](problems/91/problem.md)

[1701.Average Waiting Time](problems/1701/problem.md)

[1702.Maximum Binary String After Change](problems/1702/problem.md)

[1705.Maximum Number of Eaten Apples](problems/1705/problem.md)

[1706.Where Will the Ball Fall](problems/1706/problem.md)

[754.Reach a Number](problems/754/problem.md)

[309.Best Time to Buy and Sell Stock with Cooldown](problems/309/problem.md)

[714.Best Time to Buy and Sell Stock with Transaction Fee](problems/714/problem.md)

[1457.Pseudo-Palindromic Paths in a Binary Tree](problems/1457/problem.md)

[289.Game of Life](problems/289/problem.md)

[1328.Break a Palindrome](problems/1328/problem.md)

[808.Soup Servings](problems/808/problem.md)

[92.Reverse Linked List II](problems/92/problem.md)

[1391.Check if There is a Valid Path in a Grid](problems/1391/problem.md)

[1379.Find a Corresponding Node of a Binary Tree in a Clone of That Tree](problems/1379/problem.md)

[1711.Count Good Meals](problems/1711/problem.md)

[1712.Ways to Split Array Into Three Subarrays](problems/1712/problem.md)

[526.Beautiful Arrangement](problems/526/problem.md)

[82.Remove Duplicates from Sorted List II](problems/82/problem.md)

[399.Evaluate Division](problems/399/problem.md)

[547.Number of Provinces](problems/547/problem.md)

[3.Longest Substring Without Repeating Characters](problems/3/problem.md)

[189.Rotate Array](problems/189/problem.md)

[1717.Maximum Score From Removing Substrings](problems/1717/problem.md)

[1718.Construct the Lexicographically Largest Valid Sequence](problems/1718/problem.md)

[1721.Swapping Nodes in a Linked List](problems/1721/problem.md)

[1722.Minimize Hamming Distance After Swap Operations](problems/1722/problem.md)

[445.Add Two Numbers II](problems/445/problem.md)

[881.Boats to Save People](problems/881/problem.md)

[1658.Minimum Operations to Reduce X to Zero](problems/1658/problem.md)

[215.Kth Largest Element in an Array](problems/215/problem.md)

[470.Implement Rand10() Using Rand7()](problems/470/problem.md)

[1726.Tuple with Same Product](problems/1726/problem.md)

[1727.Largest Submatrix With Rearrangements](problems/1727/problem.md)

[1641.Count Sorted Vowel Strings](problems/1641/problem.md)

[5.Longest Palindromic Substring](problems/5/problem.md)

[1673.Find the Most Competitive Subsequence](problems/1673/problem.md)

[1657.Determine if Two Strings Are Close](problems/1657/problem.md)

[1329.Sort the Matrix Diagonally](problems/1329/problem.md)

[1733.Minimum Number of People to Teach](problems/1733/problem.md)

[1734.Decode XORed Permutation](problems/1734/problem.md)

[1738.Find Kth Largest XOR Coordinate Value](problems/1738/problem.md)

[1737.Change Minimum Characters to Satisfy One of Three Conditions](problems/1737/problem.md)

[1631.Path With Minimum Effort](problems/1631/problem.md)

[1663.Smallest String With A Given Numeric Value](problems/1663/problem.md)

[1743.Restore the Array From Adjacent Pairs](problems/1743/problem.md)

[1744.Can You Eat Your Favorite Candy on Your Favorite Day?](problems/1744/problem.md)

[31.Next Permutation](problems/31/problem.md)

[669.Trim a Binary Search Tree](problems/669/problem.md)

[142.Linked List Cycle II](problems/142/problem.md)

[71.Simplify Path](problems/71/problem.md)

[199.Binary Tree Right Side View](problems/199/problem.md)

[1749.Maximum Absolute Sum of Any Subarray](problems/1749/problem.md)

[1750.Minimum Length of String After Deleting Similar Ends](problems/1750/problem.md)

[1753.Maximum Score From Removing Stones](problems/1753/problem.md)

[1754.Largest Merge Of Two Strings](problems/1754/problem.md)

[284.Peeking Iterator](problems/284/problem.md)

[538.Convert BST to Greater Tree](problems/538/problem.md)

[1038.Binary Search Tree to Greater Sum Tree](problems/1038/problem.md)

[138.Copy List with Random Pointer](problems/138/problem.md)

[1091.Shortest Path in Binary Matrix](problems/1091/problem.md)

[1759.Count Number of Homogenous Substrings](problems/1759/problem.md)

[1760.Minimum Limit of Balls in a Bag](problems/1760/problem.md)

[785.Is Graph Bipartite?](problems/785/problem.md)

[784.Letter Case Permutation](problems/784/problem.md)

[11.Container With Most Water](problems/11/problem.md)

[413.Arithmetic Slices](problems/413/problem.md)

[1249.Minimum Remove to Make Valid Parentheses](problems/1249/problem.md)

[1764.Form Array by Concatenating Subarrays of Another Array](problems/1764/problem.md)

[1765.Map of Highest Peak](problems/1765/problem.md)

[991.Broken Calculator](problems/991/problem.md)

[1769.Minimum Number of Operations to Move All Balls to Each Box](problems/1769/problem.md)

[1770.Maximum Score from Performing Multiplication Operations](problems/1770/problem.md)

[524.Longest Word in Dictionary through Deleting](problems/524/problem.md)

[240.Search a 2D Matrix II](problems/240/problem.md)

[856.Score of Parentheses](problems/856/problem.md)

[581.Shortest Unsorted Continuous Subarray](problems/581/problem.md)

[946.Validate Stack Sequences](problems/946/problem.md)

[1774.Closest Dessert Cost](problems/1774/problem.md)

[1775.Equal Sum Arrays With Minimum Number of Operations](problems/1775/problem.md)

[304.Range Sum Query 2D - Immutable](problems/304/problem.md)

[338.Counting Bits](problems/338/problem.md)

[1780.Check if Number is a Sum of Powers of Three](problems/1780/problem.md)

[1781.Sum of Beauty of All Substrings](problems/1781/problem.md)

[1785.Minimum Elements to Add to Form a Given Sum](problems/1785/problem.md)

[1786.Number of Restricted Paths From First to Last Node](problems/1786/problem.md)

[227.Basic Calculator II](problems/227/problem.md)

[331.Verify Preorder Serialization of a Binary Tree](problems/331/problem.md)

[1791.Find Center of Star Graph](problems/1791/problem.md)

[1792.Maximum Average Pass Ratio](problems/1792/problem.md)

[54.Spiral Matrix](problems/54/problem.md)

[150.Evaluate Reverse Polish Notation](problems/150/problem.md)

[73.Set Matrix Zeroes](problems/73/problem.md)

[1797.Design Authentication Manager](problems/1797/problem.md)

[1798.Maximum Number of Consecutive Values You Can Make](problems/1798/problem.md)

[1801.Number of Orders in the Backlog](problems/1801/problem.md)

[1802.Maximum Value at a Given Index in a Bounded Array](problems/1802/problem.md)

[341.Flatten Nested List Iterator](problems/341/problem.md)

[456.132 Pattern](problems/456/problem.md)

[61.Rotate List](problems/61/problem.md)

[1806.Minimum Number of Operations to Reinitialize a Permutation](problems/1806/problem.md)

[1807.Evaluate the Bracket Pairs of a String](problems/1807/problem.md)

[74.Search a 2D Matrix](problems/74/problem.md)

[90.Subsets II](problems/90/problem.md)

[1006.Clumsy Factorial](problems/1006/problem.md)

[1143.Longest Common Subsequence](problems/1143/problem.md)

[1813.Sentence Similarity III](problems/1813/problem.md)

[1814.Count Nice Pairs in an Array](problems/1814/problem.md)

[781.Rabbits in Forest](problems/781/problem.md)

[1817.Finding the Users Active Minutes](problems/1817/problem.md)

[1818.Minimum Absolute Sum Difference](problems/1818/problem.md)

[81.Search in Rotated Sorted Array II](problems/81/problem.md)

[153.Find Minimum in Rotated Sorted Array](problems/153/problem.md)

[264.Ugly Number II](problems/264/problem.md)

[1823.Find the Winner of the Circular Game](problems/1823/problem.md)

[1824.Minimum Sideway Jumps](problems/1824/problem.md)

[179.Largest Number](problems/179/problem.md)

[208.Implement Trie (Prefix Tree)](problems/208/problem.md)

[213.House Robber II](problems/213/problem.md)

[220.Contains Duplicate III](problems/220/problem.md)

[1828.Queries on Number of Points Inside a Circle](problems/1828/problem.md)

[1829.Maximum XOR for Each Query](problems/1829/problem.md)

[1833.Maximum Ice Cream Bars](problems/1833/problem.md)

[1834.Single-Threaded CPU](problems/1834/problem.md)

[368.Largest Divisible Subset](problems/368/problem.md)

[377.Combination Sum IV](problems/377/problem.md)

[1838.Frequency of the Most Frequent Element](problems/1838/problem.md)

[1839.Longest Substring Of All Vowels in Order](problems/1839/problem.md)

[1011.Capacity To Ship Packages Within D Days](problems/1011/problem.md)

[633.Sum of Square Numbers](problems/633/problem.md)

[1845.Seat Reservation Manager](problems/1845/problem.md)

[1846.Maximum Element After Decreasing and Rearranging](problems/1846/problem.md)

[1849.Splitting a String Into Descending Consecutive Values](problems/1849/problem.md)

[1850.Minimum Adjacent Swaps to Reach the Kth Smallest Number](problems/1850/problem.md)

[554.Brick Wall](problems/554/problem.md)

[17.Letter Combinations of a Phone Number](problems/17/problem.md)

[740.Delete and Earn](problems/740/problem.md)

[1482.Minimum Number of Days to Make m Bouquets](problems/1482/problem.md)

[1855.Maximum Distance Between a Pair of Values](problems/1855/problem.md)

[1856.Maximum Subarray Min-Product](problems/1856/problem.md)

[1310.XOR Queries of a Subarray](problems/1310/problem.md)

[337.House Robber III](problems/337/problem.md)

[12.Integer to Roman](problems/12/problem.md)

[1674.Minimum Moves to Make Array Complementary](problems/1674/problem.md)

[421.Maximum XOR of Two Numbers in an Array](problems/421/problem.md)

[1860.Incremental Memory Leak](problems/1860/problem.md)

[1861.Rotating the Box](problems/1861/problem.md)

[1864.Minimum Number of Swaps to Make the Binary String Alternating](problems/1864/problem.md)

[1865.Finding Pairs With a Certain Sum](problems/1865/problem.md)

[1442.Count Triplets That Can Form Two Arrays of Equal XOR](problems/1442/problem.md)

[692.Top K Frequent Words](problems/692/problem.md)

[1035.Uncrossed Lines](problems/1035/problem.md)

[1870.Minimum Speed to Arrive on Time](problems/1870/problem.md)

[1871.Jump Game VII](problems/1871/problem.md)

[1190.Reverse Substrings Between Each Pair of Parentheses](problems/1190/problem.md)

[1669.Merge In Between Linked Lists](problems/1669/problem.md)

[1670.Design Front Middle Back Queue](problems/1670/problem.md)

[477.Total Hamming Distance](problems/477/problem.md)

[1664.Ways to Make a Fair Array](problems/1664/problem.md)

[1877.Minimize Maximum Pair Sum in Array](problems/1877/problem.md)

[1878.Get Biggest Three Rhombus Sums in a Grid](problems/1878/problem.md)

[1881.Maximum Value after Insertion](problems/1881/problem.md)

[1882.Process Tasks Using Servers](problems/1882/problem.md)

[1642.Furthest Building You Can Reach](problems/1642/problem.md)

[523.Continuous Subarray Sum](problems/523/problem.md)

[525.Contiguous Array](problems/525/problem.md)

[1653.Minimum Deletions to Make String Balanced](problems/1653/problem.md)

[474.Ones and Zeroes](problems/474/problem.md)

[1887.Reduction Operations to Make the Array Elements Equal](problems/1887/problem.md)

[1888.Minimum Number of Flips to Make the Binary String Alternating](problems/1888/problem.md)

[494.Target Sum](problems/494/problem.md)

[1049.Last Stone Weight II](problems/1049/problem.md)

[518.Coin Change 2](problems/518/problem.md)

[279.Perfect Squares](problems/279/problem.md)

[1894.Find the Student that Will Replace the Chalk](problems/1894/problem.md)

[1895.Largest Magic Square](problems/1895/problem.md)

[1898.Maximum Number of Removable Characters](problems/1898/problem.md)

[1899.Merge Triplets to Form Target Triplet](problems/1899/problem.md)

[877.Stone Game](problems/877/problem.md)

[1140.Stone Game II](problems/1140/problem.md)

[1239.Maximum Length of a Concatenated String with Unique Characters](problems/1239/problem.md)

[1904.The Number of Full Rounds You Have Played](problems/1904/problem.md)

[1905.Count Sub Islands](problems/1905/problem.md)

[1906.Minimum Absolute Difference Queries](problems/1906/problem.md)

[1600.Throne Inheritance](problems/1600/problem.md)

[1647.Minimum Deletions to Make Character Frequencies Unique](problems/1647/problem.md)

[1648.Sell Diminishing-Valued Colored Balls](problems/1648/problem.md)

[752.Open the Lock](problems/752/problem.md)

[909.Snakes and Ladders](problems/909/problem.md)

[1910.Remove All Occurrences of a Substring](problems/1910/problem.md)

[1911.Maximum Alternating Subsequence Sum](problems/1911/problem.md)

[1914.Cyclically Rotating a Grid](problems/1914/problem.md)

[1915.Number of Wonderful Substrings](problems/1915/problem.md)

[451.Sort Characters By Frequency](problems/451/problem.md)

[1921.Eliminate Maximum Number of Monsters](problems/1921/problem.md)

[1922.Count Good Numbers](problems/1922/problem.md)

[1418.Display Table of Food Orders in a Restaurant](problems/1418/problem.md)

[930.Binary Subarrays With Sum](problems/930/problem.md)

[981.Time Based Key-Value Store](problems/981/problem.md)

[274.H-Index](problems/274/problem.md)

[1926.Nearest Exit from Entrance in Maze](problems/1926/problem.md)

[1927.Sum Game](problems/1927/problem.md)

[1930.Unique Length-3 Palindromic Subsequences](problems/1930/problem.md)

[275.H-Index II](problems/275/problem.md)

[1936.Add Minimum Number of Rungs](problems/1936/problem.md)

[1937.Maximum Number of Points with Cost](problems/1937/problem.md)

[695.Max Area of Island](problems/695/problem.md)

[198.House Robber](problems/198/problem.md)

[1942.The Number of the Smallest Unoccupied Chair](problems/1942/problem.md)

[1943.Describe the Painting](problems/1943/problem.md)

[1946.Largest Number After Mutating Substring](problems/1946/problem.md)

[1947.Maximum Compatibility Score Sum](problems/1947/problem.md)

[863.All Nodes Distance K in Binary Tree](problems/863/problem.md)

[1104.Path In Zigzag Labelled Binary Tree](problems/1104/problem.md)

[1953.Maximum Number of Weeks for Which You Can Work](problems/1953/problem.md)

[1954.Minimum Garden Perimeter to Collect Enough Apples](problems/1954/problem.md)

[743.Network Delay Time](problems/743/problem.md)

[611.Valid Triangle Number](problems/611/problem.md)

[802.Find Eventual Safe States](problems/802/problem.md)

[207.Course Schedule](problems/207/problem.md)

[210.Course Schedule II](problems/210/problem.md)

[457.Circular Array Loop](problems/457/problem.md)

[1958.Check if Move is Legal](problems/1958/problem.md)

[1959.Minimum Total Space Wasted With K Resizing Operations](problems/1959/problem.md)

[1962.Remove Stones to Minimize the Total](problems/1962/problem.md)

[1963.Minimum Number of Swaps to Make the String Balanced](problems/1963/problem.md)

[313.Super Ugly Number](problems/313/problem.md)

[516.Longest Palindromic Subsequence](problems/516/problem.md)

[1583.Count Unhappy Friends](problems/1583/problem.md)

[576.Out of Boundary Paths](problems/576/problem.md)

[1968.Array With Elements Not Equal to Average of Neighbors](problems/1968/problem.md)

[1969.Minimum Non-Zero Product of the Array Elements](problems/1969/problem.md)

[443.String Compression](problems/443/problem.md)

[789.Escape The Ghosts](problems/789/problem.md)

[787.Cheapest Flights Within K Stops](problems/787/problem.md)

[797.All Paths From Source to Target](problems/797/problem.md)

[528.Random Pick with Weight](problems/528/problem.md)

## Hard

[1240.Tiling a Rectangle with the Fewest Squares](problems/1240/problem.md)

[1095.Find in Mountain Array](problems/1095/problem.md)

[188.Best Time to Buy and Sell Stock IV](problems/188/problem.md)

[1681.Minimum Incompatibility](problems/1681/problem.md)

[282.Expression Add Operators](problems/282/problem.md)

[37.Sudoku Solver](problems/37/problem.md)

[1687.Delivering Boxes from Storage to Ports](problems/1687/problem.md)

[312.Burst Balloons](problems/312/problem.md)

[1691.Maximum Height by Stacking Cuboids](problems/1691/problem.md)

[132.Palindrome Partitioning II](problems/132/problem.md)

[1463.Cherry Pickup II](problems/1463/problem.md)

[1697.Checking Existence of Edge Length Limited Paths](problems/1697/problem.md)

[639.Decode Ways II](problems/639/problem.md)

[1703.Minimum Adjacent Swaps for K Consecutive Ones](problems/1703/problem.md)

[1707.Maximum XOR With an Element From Array](problems/1707/problem.md)

[1345.Jump Game IV](problems/1345/problem.md)

[123.Best Time to Buy and Sell Stock III](problems/123/problem.md)

[84.Largest Rectangle in Histogram](problems/84/problem.md)

[920.Number of Music Playlists](problems/920/problem.md)

[1713.Minimum Operations to Make a Subsequence](problems/1713/problem.md)

[878.Nth Magical Number](problems/878/problem.md)

[410.Split Array Largest Sum](problems/410/problem.md)

[127.Word Ladder](problems/127/problem.md)

[1719.Number Of Ways To Reconstruct A Tree](problems/1719/problem.md)

[1723.Find Minimum Time to Finish All Jobs](problems/1723/problem.md)

[1649.Create Sorted Array through Instructions](problems/1649/problem.md)

[1728.Cat and Mouse II](problems/1728/problem.md)

[1735.Count Ways to Make Array With Product](problems/1735/problem.md)

[1739.Building Boxes](problems/1739/problem.md)

[987.Vertical Order Traversal of a Binary Tree](problems/987/problem.md)

[1675.Minimize Deviation in Array](problems/1675/problem.md)

[1745.Palindrome Partitioning IV](problems/1745/problem.md)

[1751.Maximum Number of Events That Can Be Attended II](problems/1751/problem.md)

[1755.Closest Subsequence Sum](problems/1755/problem.md)

[1761.Minimum Degree of a Connected Trio in a Graph](problems/1761/problem.md)

[51.N-Queens](problems/51/problem.md)

[52.N-Queens II](problems/52/problem.md)

[1766.Tree of Coprimes](problems/1766/problem.md)

[1771.Maximize Palindrome Length From Subsequences](problems/1771/problem.md)

[1776.Car Fleet II](problems/1776/problem.md)

[895.Maximum Frequency Stack](problems/895/problem.md)

[354.Russian Doll Envelopes](problems/354/problem.md)

[1782.Count Pairs Of Nodes](problems/1782/problem.md)

[1793.Maximum Score of a Good Subarray](problems/1793/problem.md)

[1787.Make the XOR of All Segments Equal to Zero](problems/1787/problem.md)

[115.Distinct Subsequences](problems/115/problem.md)

[1799.Maximize Score After N Operations](problems/1799/problem.md)

[1803.Count Pairs With XOR in a Range](problems/1803/problem.md)

[1808.Maximize Number of Nice Divisors](problems/1808/problem.md)

[42.Trapping Rain Water42. Trapping Rain Water](problems/42/problem.md)

[154.Find Minimum in Rotated Sorted Array II](problems/154/problem.md)

[1825.Finding MK Average](problems/1825/problem.md)

[87.Scramble String](problems/87/problem.md)

[1835.Find XOR Sum of All Pairs Bitwise AND](problems/1835/problem.md)

[363.Max Sum of Rectangle No Larger Than K](problems/363/problem.md)

[1840.Maximum Building Height](problems/1840/problem.md)

[403.Frog Jump](problems/403/problem.md)

[1847.Closest Room](problems/1847/problem.md)

[1851.Minimum Interval to Include Each Query](problems/1851/problem.md)

[1473.Paint House III](problems/1473/problem.md)

[1857.Largest Color Value in a Directed Graph](problems/1857/problem.md)

[1815.Maximum Number of Groups Getting Fresh Donuts](problems/1815/problem.md)

[1819.Number of Different Subsequences GCDs](problems/1819/problem.md)

[1269.Number of Ways to Stay in the Same Place After Some Steps](problems/1269/problem.md)

[1862.Sum of Floored Pairs](problems/1862/problem.md)

[1866.Number of Ways to Rearrange Sticks With K Sticks Visible](problems/1866/problem.md)

[810.Chalkboard XOR Game](problems/810/problem.md)

[1872.Stone Game VIII](problems/1872/problem.md)

[664.Strange Printer](problems/664/problem.md)

[1671.Minimum Number of Removals to Make Mountain Array](problems/1671/problem.md)

[1665.Minimum Initial Energy to Finish Tasks](problems/1665/problem.md)

[1074.Number of Submatrices That Sum to Target](problems/1074/problem.md)

[1879.Minimum XOR Sum of Two Arrays](problems/1879/problem.md)

[1883.Minimum Skips to Arrive at Meeting On Time](problems/1883/problem.md)

[1659.Maximize Grid Happiness](problems/1659/problem.md)

[1643.Kth Smallest Instructions](problems/1643/problem.md)

[1889.Minimum Space Wasted From Packaging](problems/1889/problem.md)

[879.Profitable Schemes](problems/879/problem.md)

[1655.Distribute Repeating Integers](problems/1655/problem.md)

[1449.Form Largest Integer With Digits That Add up to Target](problems/1449/problem.md)

[1896.Minimum Cost to Change the Final Value of Expression](problems/1896/problem.md)

[1900.The Earliest and Latest Rounds Where Players Compete](problems/1900/problem.md)

[1406.Stone Game III](problems/1406/problem.md)

[1510.Stone Game IV](problems/1510/problem.md)

[65.Valid Number](problems/65/problem.md)

[1563.Stone Game V](problems/1563/problem.md)

[483.Smallest Good Base](problems/483/problem.md)

[149.Max Points on a Line](problems/149/problem.md)

[773.Sliding Puzzle](problems/773/problem.md)

[1912.Design Movie Rental System](problems/1912/problem.md)

[1916.Count Ways to Build Rooms in an Ant Colony](problems/1916/problem.md)

[815.Bus Routes](problems/815/problem.md)

[297.Serialize and Deserialize Binary Tree](problems/297/problem.md)

[1923.Longest Common Subpath](problems/1923/problem.md)

[726.Number of Atoms](problems/726/problem.md)

[887.Super Egg Drop](problems/887/problem.md)

[1928.Minimum Cost to Reach Destination in Time](problems/1928/problem.md)

[1931.Painting a Grid With Three Different Colors](problems/1931/problem.md)

[1932.Merge BSTs to Create Single BST](problems/1932/problem.md)

[218.The Skyline Problem](problems/218/problem.md)

[1938.Maximum Genetic Difference Query](problems/1938/problem.md)

[1944.Number of Visible People in a Queue](problems/1944/problem.md)

[1948.Delete Duplicate Folders in System](problems/1948/problem.md)

[1955.Count Number of Special Subsequences](problems/1955/problem.md)

[847.Shortest Path Visiting All Nodes](problems/847/problem.md)

[1964.Find the Longest Valid Obstacle Course at Each Position](problems/1964/problem.md)

[446.Arithmetic Slices II - Subsequence](problems/446/problem.md)

[1970.Last Day Where You Can Still Cross](problems/1970/problem.md)

[552.Student Attendance Record II](problems/552/problem.md)

[295.Find Median from Data Stream](problems/295/problem.md)

## Mysql

[1179.Reformat Department Table](problems/1179/problem.md)

## LCP

[01.猜数字](problems/LCP/01/problem.md)

[02.分式化简](problems/LCP/02/problem.md)

[03.机器人大冒险](problems/LCP/03/problem.md)

[04.覆盖](problems/LCP/04/problem.md)

[07.传递信息](problems/LCP/07/problem.md)

[28.采购方案](problems/LCP/28/problem.md)

[29.乐团站位](problems/LCP/29/problem.md)

[30.魔塔游戏](problems/LCP/30/problem.md)

[31.变换的迷宫](problems/LCP/31/problem.md)

[32.批量处理任务](problems/LCP/32/problem.md)

[33.蓄水](problems/LCP/33/problem.md)

[34.二叉树染色](problems/LCP/34/problem.md)

[35.电动车游城市](problems/LCP/35/problem.md)

[36.最多牌组数](problems/LCP/36/problem.md)

## Interview

[03.01.三合一](problems/Interview/03_01/problem.md)

[10.02.变位词组](problems/Interview/10_02/problem.md)

[17.10.主要元素](problems/Interview/17_10/problem.md)

[17.21.直方图的水量](problems/Interview/17_21/problem.md)

## 剑指 Offer

[38.字符串的排列](problems/剑指Offer/38/problem.md)

[42.连续子数组的最大和](problems/剑指Offer/42/problem.md)

[52.两个链表的第一个公共节点](problems/剑指Offer/52/problem.md)

[53-I.在排序数组中查找数字 I](problems/剑指Offer/53-I/problem.md)
