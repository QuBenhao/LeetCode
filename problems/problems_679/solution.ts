function judgePoint24(cards: number[]): boolean {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const cards: number[] = JSON.parse(inputValues[0]);
	return judgePoint24(cards);
}
