function findAllPeople(n: number, meetings: number[][], firstPerson: number): number[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	const meetings: number[][] = JSON.parse(inputValues[1]);
	const firstPerson: number = JSON.parse(inputValues[2]);
	return findAllPeople(n, meetings, firstPerson);
}
