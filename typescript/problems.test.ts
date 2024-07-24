import * as fs from 'fs';
import * as ts from "typescript";

var _ = require('lodash-contrib');
const vm = require('node:vm');
import {CompareResults} from "./common";

const PROBLEMS: string[][] = [['49', 'problems']];

for (const [problemId, problemFolder] of PROBLEMS) {
    describe(`Test for problem ${problemId}`, () => {
        let inputJson: any;
        let outputJson: any;
        let script: any;

        beforeAll(async () => {
            let testCasePath = `${problemFolder}/${problemFolder}_${problemId}/testcase`;
            let solPath: string = `${problemFolder}/${problemFolder}_${problemId}/solution.ts`;
            if (!fs.existsSync(testCasePath)) {
                console.log(`Problem in ${problemFolder} not found, try premiums...`);
                testCasePath = `premiums/premiums_${problemId}/testcase`;
                solPath = `premiums/premiums_${problemId}/solution.ts`;
            }
            const fileContent: string = fs.readFileSync(testCasePath, "utf-8");
            const splits: string[] = fileContent.split("\n");
            const inputs: string = splits[0], outputs: string = splits[1];
            inputJson = JSON.parse(inputs);
            outputJson = JSON.parse(outputs);
            let solutionFileContent: string = fs.readFileSync(solPath, "utf-8");
            solutionFileContent = solutionFileContent.split('\n').filter(line => !line.trim().startsWith('import ')).join('\n');
            solutionFileContent = solutionFileContent.replace("export function Solve", "function Solve");
            solutionFileContent += "const execResult = Solve(testInputJsonString);"
            let result = ts.transpileModule(solutionFileContent, {
                compilerOptions: {
                    module: ts.ModuleKind.ES2022,
                    downlevelIteration: true
                }
            });
            const codeText: string = result["outputText"];
            script = new vm.Script(codeText);
        });

        test(`Test solution ${problemId}`, () => {
            expect(script).toBeDefined();
            for (let i: number = 0; i < inputJson.length; i++) {
                CompareResults(script, inputJson[i], outputJson[i]);
            }
        })
    });
}

