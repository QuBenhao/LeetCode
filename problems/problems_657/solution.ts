function judgeCircle(moves: string): boolean {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const moves: string = JSON.parse(inputValues[0]);
	return judgeCircle(moves);
}
