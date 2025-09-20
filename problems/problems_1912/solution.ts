class MovieRentingSystem {
    constructor(n: number, entries: number[][]) {
        
    }

    search(movie: number): number[] {
        
    }

    rent(shop: number, movie: number): void {
        
    }

    drop(shop: number, movie: number): void {
        
    }

    report(): number[][] {
        
    }
}

/**
 * Your MovieRentingSystem object will be instantiated and called as such:
 * var obj = new MovieRentingSystem(n, entries)
 * var param_1 = obj.search(movie)
 * obj.rent(shop,movie)
 * obj.drop(shop,movie)
 * var param_4 = obj.report()
 */

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const operators: string[] = JSON.parse(inputValues[0]);
	const opValues: any[][] = JSON.parse(inputValues[1]);
	const ans: any[] = [null];
	const obj: MovieRentingSystem = new MovieRentingSystem(opValues[0][0], opValues[0][1]);
	for (let i: number = 1; i < operators.length; i++) {
		if (operators[i] == "search") {
			ans.push(obj.search(opValues[i][0]));
			continue;
		}
		if (operators[i] == "rent") {
			obj.rent(opValues[i][0], opValues[i][1]);
			ans.push(null);
			continue;
		}
		if (operators[i] == "drop") {
			obj.drop(opValues[i][0], opValues[i][1]);
			ans.push(null);
			continue;
		}
		if (operators[i] == "report") {
			ans.push(obj.report());
			continue;
		}
		ans.push(null);
	}
	return ans;
}
