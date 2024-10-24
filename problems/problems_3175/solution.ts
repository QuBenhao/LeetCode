function findWinningPlayer(skills: number[], k: number): number {
    let ans: number = 0, cur: number = 0;
	const n: number = skills.length;
	for (let i: number = 1; i < n; i++) {
		if (skills[i] < skills[ans]) {
			cur++;
		} else {
			cur = 1;
			ans = i;
		}
		if (cur == k) {
			break;
		}
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const skills: number[] = JSON.parse(inputValues[0]);
	const k: number = JSON.parse(inputValues[1]);
	return findWinningPlayer(skills, k);
}
