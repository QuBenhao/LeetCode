class Router {
    constructor(memoryLimit: number) {
        
    }

    addPacket(source: number, destination: number, timestamp: number): boolean {
        
    }

    forwardPacket(): number[] {
        
    }

    getCount(destination: number, startTime: number, endTime: number): number {
        
    }
}

/**
 * Your Router object will be instantiated and called as such:
 * var obj = new Router(memoryLimit)
 * var param_1 = obj.addPacket(source,destination,timestamp)
 * var param_2 = obj.forwardPacket()
 * var param_3 = obj.getCount(destination,startTime,endTime)
 */

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const operators: string[] = JSON.parse(inputValues[0]);
	const opValues: any[][] = JSON.parse(inputValues[1]);
	const ans: any[] = [null];
	const obj: Router = new Router(opValues[0][0]);
	for (let i: number = 1; i < operators.length; i++) {
		if (operators[i] == "addPacket") {
			ans.push(obj.addPacket(opValues[i][0], opValues[i][1], opValues[i][2]));
			continue;
		}
		if (operators[i] == "forwardPacket") {
			ans.push(obj.forwardPacket());
			continue;
		}
		if (operators[i] == "getCount") {
			ans.push(obj.getCount(opValues[i][0], opValues[i][1], opValues[i][2]));
			continue;
		}
		ans.push(null);
	}
	return ans;
}
