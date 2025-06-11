# Java

## Start

First install maven environment,

**change daily in [daily.json](../daily-problems.json)** `Note: the json file is under root with your problem folder, named 'daily-${folder}.json'` and try:
```shell
mvn test -Dtest="qubhjava.test.TestMain"
```

or if you want to run more than one questions,
**change plans in [daily.json](../daily-problems.json)** `Note: the json file is under root with your problem folder, named 'daily-${folder}.json'` and try:
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