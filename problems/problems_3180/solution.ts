function maxTotalReward(rewardValues: number[]): number {
    rewardValues.sort((a, b) => a - b);
    let f = BigInt(1);
    for (let x of rewardValues) {
        let mask = (BigInt(1) << BigInt(x)) - BigInt(1);
        f = f | ((f & mask) << BigInt(x));
    }
    return f.toString(2).length - 1;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const rewardValues: number[] = JSON.parse(inputValues[0]);
	return maxTotalReward(rewardValues);
}
