import * as fs from 'fs';
import * as dotenv from 'dotenv'

var _ = require('lodash-contrib');


const PROBLEM_ID: string = "699";
import {Solve} from "../problems/problems_699/solution";
// import {Solve} from "../premiums/premiums_1056/solution";

describe("TestMain===" + PROBLEM_ID, () => {
    dotenv.config();
    let problemFolder: string = (process.env.PROBLEM_FOLDER && process.env.PROBLEM_FOLDER.length > 0) ? process.env.PROBLEM_FOLDER : "problems";
    let testCasePath: string = `${problemFolder}/${problemFolder}_${PROBLEM_ID}/testcase`;
    if (!fs.existsSync(testCasePath)) {
        console.log(`Problem in ${problemFolder} not found, try premiums...`);
        testCasePath = `premiums/premiums_${PROBLEM_ID}/testcase`
    }
    const fileContent: string = fs.readFileSync(testCasePath, "utf-8");
    const splits: string[] = fileContent.split("\n");
    const inputs: string = splits[0], outputs: string = splits[1];
    const inputJson: any = JSON.parse(inputs), outputJson: any = JSON.parse(outputs);
    for (let i: number = 0; i < inputJson.length; i++) {
        it("TestCase" + i, () => {
            if (_.isFloat(outputJson[i])) {
                expect(Solve(inputJson[i])).toBeCloseTo(outputJson[i]);
            } else {
                expect(Solve(inputJson[i])).toEqual(outputJson[i]);
            }
        })
    }
})