# Java

## Start

First install maven environment,

**change problem sentence `import problems.problems_2028.Solution;` and `private static final String PROBLEM_ID = "2710";` in [TestMain.java](test/TestMain.java)**, and try:
```shell
mvn test -Dtest="qubhjava.test.TestMain"
```

or if you want to run more than one questions,
**change problem and problem folder `private static final String[][] PROBLEMS = {{"1", "problems"}, {"2", "problems"}};` in [ProblemsTest.java](test/ProblemsTest.java)**, and try:
```shell
mvn test -Dtest="qubhjava.test.ProblemsTest"
```