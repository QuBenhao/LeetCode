# Typescript

## Start

First install npm environment at root, recommend using npm v10.7.0 and node v20.15.1

```shell
npm install
```

**change daily in [daily.json](../daily-problems.json)** `Note: the json file is under root with your problem folder, named 'daily-${folder}.json'` and try at root:

```shell
npm test --alwaysStrict --strictBindCallApply --strictFunctionTypes --target ES2022 typescript/test.ts
```

or if you want to run more than one questions,
**change plans in [daily.json](../daily-problems.json)** `Note: the json file is under root with your problem folder, named 'daily-${folder}.json'` and try:
```shell
npm test --alwaysStrict --strictBindCallApply --strictFunctionTypes --target ES2022 typescript/problems.test.ts
```
