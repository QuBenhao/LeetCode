function maxmiumScore(cards: number[], cnt: number): number {
	cards.sort((a, b) => b - a);
	let sum: number = 0;
	for (let i: number = 0; i < cnt; i++) {
		sum += cards[i];
	}
	if (sum % 2 === 0) {
		return sum;
	}
	const cur: number = cards[cnt - 1];
	const replaceSum: Function = (x: number): number => {
		for (let i: number = cnt; i < cards.length; i++) {
			if (cards[i] % 2 !== x % 2) {
				return sum - x + cards[i];
			}
		}
		return 0;
	}
	let ans: number = replaceSum(cur);
	for (let i: number = cnt - 2; i >= 0; i--) {
		if (cards[i] % 2 !== cur % 2) {
			ans = Math.max(ans, replaceSum(cards[i]));
			break;
		}
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const cards: number[] = JSON.parse(inputValues[0]);
	const cnt: number = JSON.parse(inputValues[1]);
	return maxmiumScore(cards, cnt);
}
