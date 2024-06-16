import * as fs from 'fs';

const PROBLEM_ID: string = "57"
import {Solve} from "../../problems/problems_57/solution";

describe("TestMain===" + PROBLEM_ID, () => {
    const fileContent = fs.readFileSync(`../problems/problems_${PROBLEM_ID}/testcase`, "utf-8");
    const splits: string[] = fileContent.split("\n");
    const inputs: string = splits[0], outputs: string = splits[1];
    const inputJson = JSON.parse(inputs), outputJson = JSON.parse(outputs);
    for (let i = 0; i < inputJson.length; i++) {
        it("TestCase" + i, () => {
            expect(Solve(inputJson[i])).toEqual(outputJson[i]);
        })
    }
})