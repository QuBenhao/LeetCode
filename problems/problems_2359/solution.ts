function closestMeetingNode(edges: number[], node1: number, node2: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const edges: number[] = JSON.parse(inputValues[0]);
	const node1: number = JSON.parse(inputValues[1]);
	const node2: number = JSON.parse(inputValues[2]);
	return closestMeetingNode(edges, node1, node2);
}
