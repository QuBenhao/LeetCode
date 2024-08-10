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

** If you are facing errors from problems folder Java file **, add these to [pom.xml](../pom.xml)
```xml
                <configuration>
                    <source>21</source>
                    <target>21</target>
                    <excludes>
                        <exclude>bazel-*/**</exclude>
                        <exclude>problems/**</exclude>
                        <exclude>premiums/**</exclude>
                    </excludes>
                </configuration>
```