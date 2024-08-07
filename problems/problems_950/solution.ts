function deckRevealedIncreasing(deck: number[]): number[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const deck: number[] = JSON.parse(inputValues[0]);
	return deckRevealedIncreasing(deck);
}
