function maxAverageRatio(classes: number[][], extraStudents: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const classes: number[][] = JSON.parse(inputValues[0]);
	const extraStudents: number = JSON.parse(inputValues[1]);
	return maxAverageRatio(classes, extraStudents);
}
