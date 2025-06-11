import * as fs from 'fs';
import * as dotenv from 'dotenv'
import * as ts from "typescript";

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
const PROBLEM_ID: string = dailyProblems.daily;

describe("TestMain===" + PROBLEM_ID, () => {
    dotenv.config();
    let problemFolder: string = (process.env.PROBLEM_FOLDER && process.env.PROBLEM_FOLDER.length > 0) ? process.env.PROBLEM_FOLDER : "problems";
    let testCasePath: string = `${problemFolder}/${problemFolder}_${PROBLEM_ID}/testcase`;
    let solPath: string = `${problemFolder}/${problemFolder}_${PROBLEM_ID}/solution.ts`;
    if (!fs.existsSync(testCasePath)) {
        console.log(`Problem in ${problemFolder} not found, try premiums...`);
        testCasePath = `premiums/premiums_${PROBLEM_ID}/testcase`
        solPath = `premiums/premiums_${PROBLEM_ID}/solution.ts`;
    }
    const testcaseFileContent: string = fs.readFileSync(testCasePath, "utf-8");
    const splits: string[] = testcaseFileContent.split("\n");
    const inputs: string = splits[0], outputs: string = splits[1];
    const inputJson: any = JSON.parse(inputs), outputJson: any = JSON.parse(outputs);
    expect(inputJson.length).toBeGreaterThan(0);
    let fileContent: string = fs.readFileSync(solPath, "utf-8");
    let nodeClass: String = null;
    for (const line of fileContent.split('\n')) {
        if (line.startsWith("import ")) {
            if (line.indexOf("typescript/models/node.") != -1) {
                nodeClass = line.split(" as _Node")[0].split(",").pop().trim();
                break;
            }
        }
    }
    fileContent = fileContent.split('\n').filter(line => !line.trim().startsWith('import ')).join('\n');
    fileContent = fileContent.replace("export function Solve", "function Solve");
    fileContent += "const execResult = Solve(testInputJsonString);"
    let result = ts.transpileModule(fileContent, {
        compilerOptions: {
            module: ts.ModuleKind.ES2022,
            downlevelIteration: true
        }
    });

    const r = result["outputText"];
    const script = new vm.Script(r);
    for (let i: number = 0; i < inputJson.length; i++) {
        it("TestCase" + i, () => {
            CompareResults(script, inputJson[i], outputJson[i], nodeClass);
        })
    }
})
