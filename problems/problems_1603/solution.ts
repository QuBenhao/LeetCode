class ParkingSystem {
    parks: number[]
    constructor(big: number, medium: number, small: number) {
        this.parks = [big, medium, small];
    }

    addCar(carType: number): boolean {
        if (this.parks[--carType] <= 0) {
            return false;
        }
        this.parks[carType]--;
        return true;
    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * var obj = new ParkingSystem(big, medium, small)
 * var param_1 = obj.addCar(carType)
 */

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const operators: string[] = JSON.parse(splits[0]);
	const values: any[][] = JSON.parse(splits[1]);
	const ans: any[] = [null];
	const obj: ParkingSystem = new ParkingSystem(values[0][0], values[0][1], values[0][2]);
	for (let i: number = 1; i < operators.length; i++) {
		if (operators[i] == "addCar") {
			ans.push(obj.addCar(values[i][0]));
			continue;
		}
		ans.push(null);
	}
	return ans;
}
