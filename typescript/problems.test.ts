import * as fs from 'fs';
import * as ts from "typescript";
import * as path from "path"; // <-- Add this import

var _ = require('lodash-contrib');
const vm = require('node:vm');
import {CompareResults} from "./common";

const envContent: string = fs.readFileSync('.env', 'utf-8');

// get PROBLEM_FOLDER from .env file
var problemFolder: string = "problems";
for (const line of envContent.split('\n')) {
    if (line.startsWith("PROBLEM_FOLDER=")) {
        problemFolder = line.split('=')[1].trim();
        break;
    }
}

// open daily-${problemFolder}.json
const dailyFilePath: string = `daily-${problemFolder}.json`;
let dailyFileContent: string = '';
if (fs.existsSync(dailyFilePath)) {
    dailyFileContent = fs.readFileSync(dailyFilePath, 'utf-8');
} else {
    console.log(`File ${dailyFilePath} not found, using default problems...`);
    dailyFileContent = fs.readFileSync('daily-problems.json', 'utf-8');
}
// parse daily-${problemFolder}.json
const dailyProblems: any = JSON.parse(dailyFileContent);
const plans = dailyProblems.plans || [];

for (let i: number = 0; i < plans.length; i += 2) {
    const problemId: string = plans[i];
    const problemFolder: string = plans[i + 1];
    describe(`Test for problem ${problemId}`, () => {
        let inputJson: any;
        let outputJson: any;
        let script: any;
        let nodeClass: String = null;

        beforeAll(async () => {
            let testCasePath: string = path.join(problemFolder, `${problemFolder}_${problemId}`, 'testcase');
            let solPath: string = path.join(problemFolder, `${problemFolder}_${problemId}`, 'solution.ts');
            if (!fs.existsSync(testCasePath)) {
                console.log(`Problem in ${problemFolder} not found, try premiums...`);
                testCasePath = path.join('premiums', `premiums_${problemId}`, 'testcase');
                solPath = path.join('premiums', `premiums_${problemId}`, 'solution.ts');
            }
            const fileContent: string = fs.readFileSync(testCasePath, "utf-8");
            const splits: string[] = fileContent.split("\n");
            const inputs: string = splits[0], outputs: string = splits[1];
            inputJson = JSON.parse(inputs);
            outputJson = JSON.parse(outputs);
            let solutionFileContent: string = fs.readFileSync(solPath, "utf-8");
            for (const line of solutionFileContent.split('\n')) {
                if (line.startsWith("import ")) {
                    // import {JSONArrayToNodeRandom,NodeRandom as _Node,NodeRandomToJSONArray} from "../../typescript/models/node.random";
                    if (line.indexOf("typescript/models/node.") != -1) {
                        nodeClass = line.split(" as _Node")[0].split(",").pop().trim();
                        break;
                    }
                }
            }
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
            expect(inputJson.length).toBeGreaterThan(0);
            for (let i: number = 0; i < inputJson.length; i++) {
                CompareResults(script, inputJson[i], outputJson[i], nodeClass);
            }
        })
    });
}

