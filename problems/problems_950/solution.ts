function deckRevealedIncreasing(deck: number[]): number[] {
	const q: Array<number> = [];
	deck.sort((a, b) => b - a);
	for (let i: number = 0; i < deck.length; i++) {
		if (q.length > 0) {
			q.unshift(q.pop());
		}
		q.unshift(deck[i]);
	}
	return q;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const deck: number[] = JSON.parse(inputValues[0]);
	return deckRevealedIncreasing(deck);
}
