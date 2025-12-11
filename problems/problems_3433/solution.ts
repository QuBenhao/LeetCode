function countMentions(numberOfUsers: number, events: string[][]): number[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const numberOfUsers: number = JSON.parse(inputValues[0]);
	const events: string[][] = JSON.parse(inputValues[1]);
	return countMentions(numberOfUsers, events);
}
