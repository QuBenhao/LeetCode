# Java

## Start

First install maven environment,

**change problem sentence `import problems.problems_2028.Solution;` and `private static final String PROBLEM_ID = "2710";` in [TestMain.java](test/TestMain.java)**, and try:
```shell
mvn test -Dtest="qubhjava.test.TestMain"
```

** If you are facing errors from problems folder Java file **, add thest to [pom.xml](../pom.xml)
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