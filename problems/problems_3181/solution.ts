function maxTotalReward(rewardValues: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const rewardValues: number[] = JSON.parse(inputValues[0]);
	return maxTotalReward(rewardValues);
}
