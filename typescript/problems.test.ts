import * as fs from 'fs';

var _ = require('lodash-contrib');


const PROBLEMS: string[][] = [['560', 'problems']];

for (const [problemId, problemFolder] of PROBLEMS) {
    describe(`Test for problem ${problemId}`, () => {
        let Solve: any;
        let inputJson: any;
        let outputJson: any;

        beforeAll(async () => {
            let testCasePath = `${problemFolder}/${problemFolder}_${problemId}/testcase`;
            if (!fs.existsSync(testCasePath)) {
                console.log(`Problem in ${problemFolder} not found, try premiums...`);
                testCasePath = `premiums/premiums_${problemId}/testcase`;
            }
            const fileContent: string = fs.readFileSync(testCasePath, "utf-8");
            const splits: string[] = fileContent.split("\n");
            const inputs: string = splits[0], outputs: string = splits[1];
            inputJson = JSON.parse(inputs);
            outputJson = JSON.parse(outputs);

            const solution = await import(`../${problemFolder}/${problemFolder}_${problemId}/solution`);
            Solve = solution.Solve;
        });

        test(`Test solution ${problemId}`, () => {
            expect(Solve).toBeDefined();
            for (let i: number = 0; i < inputJson.length; i++) {
                if (_.isFloat(outputJson[i])) {
                    expect(Solve(inputJson[i])).toBeCloseTo(outputJson[i]);
                } else {
                    expect(Solve(inputJson[i])).toEqual(outputJson[i]);
                }
            }
        })
    });
}