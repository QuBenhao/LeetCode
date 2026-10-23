function countDaysTogether(arriveAlice: string, leaveAlice: string, arriveBob: string, leaveBob: string): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const arriveAlice: string = JSON.parse(inputValues[0]);
	const leaveAlice: string = JSON.parse(inputValues[1]);
	const arriveBob: string = JSON.parse(inputValues[2]);
	const leaveBob: string = JSON.parse(inputValues[3]);
	return countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob);
}
