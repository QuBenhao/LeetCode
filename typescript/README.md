# Typescript

## Start

First install npm environment at root, recommend using npm v10.7.0 and node v20.15.1

```shell
npm install
```

**change problem sentence
`const PROBLEM_ID: string = "${}";
import {Solve} from "../problems/problems_${}/solution";`
in [test.ts](test.ts)**, and try at root:

```shell
npm test --alwaysStrict --strictBindCallApply --strictFunctionTypes --target ES2022 typescript/test.ts
```

or if you want to run more than one questions,
**change problem and problem folder `const PROBLEMS: string[][] = [["1", "problems"], ["2", "problems"]];` in [problems.test.ts](problems.test.ts)**, and try:
```shell
npm test --alwaysStrict --strictBindCallApply --strictFunctionTypes --target ES2022 typescript/problems.test.ts
```
