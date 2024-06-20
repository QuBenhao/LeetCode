import * as fs from 'fs';
var _ = require('lodash-contrib');


const PROBLEM_ID: string = "LCP 61";
import {Solve} from "../problems/problems_LCP 61/solution";
// import {Solve} from "../premiums/premiums_422/solution";

describe("TestMain===" + PROBLEM_ID, () => {
    let testCasePath: string = `problems/problems_${PROBLEM_ID}/testcase`;
    if (!fs.existsSync(testCasePath)) {
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